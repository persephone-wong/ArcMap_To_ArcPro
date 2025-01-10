# Script Name: AllChart.py
# Created by Babak Kasraei (modified by Sarah Bartnik)
# Date: Feb 28,2013 / March 25, 2013
# Description: This script will find the extents in the current map and add all 
# charts to the related biggest extent in the map view

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
legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT", "Legend")[0]

#The DataFrame extent object is converted into a polygon feature so it can be used with the SelectLayerByLocation function.
dfAsFeature = arcpy.Polygon(arcpy.Array([df.extent.lowerLeft, df.extent.lowerRight, df.extent.upperRight, df.extent.upperLeft]),
                            df.spatialReference)
arcpy.SelectLayerByLocation_management(lyr, "WITHIN", dfAsFeature, "", "NEW_SELECTION")

 # Create the search cursor
#
cur = arcpy.SearchCursor(lyr)
# Search the  chart folder

folder = os.listdir("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/")
        
# this double loop will match chart files and chart numbers in the extent layer
for row in cur:
    for file in folder:
        if row.CHARTNO+".KAP" == file:
           chart = os.path.join("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts", row.CHARTNO+".KAP" )
           addLayer = arcpy.mapping.Layer(chart)
           # <SB> This line turns off the automatic addition of the layers to the legend 
           legend.autoAdd = True
           # <SB> This line adds charts to the Charts group layer in the TOC
           arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, addLayer, "TOP")
           arcpy.RefreshActiveView()
           arcpy.RefreshTOC()


arcpy.SelectLayerByAttribute_management("CHS Raster Chart" ,"CLEAR_SELECTION")
# <SB> This line is supposed to return the AutoAdd to legend property back on
legend.autoAdd = False

#This loop changes the chart group's symbology
for lyr in targetGroupLayer:
   symbologyLayer = "Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/Chart_Symbology.lyr"
   arcpy.ApplySymbologyFromLayer_management(lyr, symbologyLayer)
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
