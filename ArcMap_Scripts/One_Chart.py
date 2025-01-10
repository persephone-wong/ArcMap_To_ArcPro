#Script name: OneChart.py
#
#Date: March 07,2013 / March 25, 2013 / April 03, 2013
#Created by Babak Kasraei (modified by Sarah Bartnik) (modified by S. yee)
# Description: This script will add the largest chart to the map extent.



# Import modules
import sys,os,math,string,arcpy
from arcpy import env

# Read from current map
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Data Themes")[0]
lyr = arcpy.mapping.ListLayers(mxd, "CHS Raster Chart", df)[0]
# <SB> This line defines the group layer where charts are to be put once loaded
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Charts", df)[0]
# <SB> This line defines the legend element
legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT", "Legend")[0]#The DataFrame extent object is converted into a polygon feature so it can be used with the SelectLayerByLocation function.
dfAsFeature = arcpy.Polygon(arcpy.Array([df.extent.lowerLeft, df.extent.lowerRight, df.extent.upperRight, df.extent.upperLeft]),
                            df.spatialReference)
# Select the extents into the df map view
arcpy.SelectLayerByLocation_management(lyr, "WITHIN", dfAsFeature, "", "NEW_SELECTION")

 # Create the search cursor
#
cur = arcpy.SearchCursor(lyr)
# This list will keep the numbers
featureList = []
#This loop will go through rows to find the biggest chart Number 
for row in cur:
   featureList.append(row.CHARTSCALE)
# This is the maximum scale in mapview
MX = max(featureList)
#Charts are here
folder = os.listdir("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/")
cur = arcpy.SearchCursor(lyr)

# This loop will add the chart
for row in cur:
   for file in folder:
      if row.CHARTSCALE == MX:
         chart = os.path.join("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/", row.CHARTNO+".KAP" )
addLayer = arcpy.mapping.Layer(chart)
# <SB> This line turns off the automatic addition of the layers to the legend 
legend.autoAdd = False
# <SB> This line adds charts to the Charts group layer in the TOC
arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, addLayer, "TOP")
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
# Process: deSelect Layer By Location
arcpy.SelectLayerByAttribute_management(lyr,"CLEAR_SELECTION")
# <SB> This line is supposed to return the AutoAdd to legend property back on
legend.autoAdd = True

#This loop changes the chart group's symbology
for lyr in targetGroupLayer:
   symbologyLayer = "Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/Chart_Symbology.lyr"
   arcpy.ApplySymbologyFromLayer_management(lyr, symbologyLayer)
arcpy.RefreshActiveView()
arcpy.RefreshTOC()

                              