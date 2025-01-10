# ---------------------------------------------------------------------------
# select_by_sector.py
# Created on: 2013-04-26 
# Created by: Sarah Bartnik  
# Description: 
# Process to select features within a specified sector (file geodatabase)
# ---------------------------------------------------------------------------

# Import arcpy and python modules
import sys,os,math,string,arcpy
from arcpy import env

# Script arguments
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Data Themes")[0]

# Collects parameter from user and converts it to uppercase text
getFilters = arcpy.GetParameter(0)
queryList = "','".join(getFilters)

# Collects list of layers from user
getLayers = arcpy.GetParameter(1)

# Puts the parameter string and the field string in the definition query box for the Sectors feature
if len(getFilters) > 0:
    for lyr in arcpy.mapping.ListLayers(mxd):
        if lyr.name == "Sectors":
	        lyr.definitionQuery = '"SECTOR" in (\'{0}\')' .format(queryList.upper())

# Call ArcPy tool to select features by location
for lyr2 in getLayers:
    if lyr2.isFeatureLayer == True :
        arcpy.AddMessage("Now selecting features from: " + lyr2.name)    
        arcpy.SelectLayerByLocation_management(lyr2.name,"WITHIN",'Sectors')

#Refresh the screen and zoom to the selected features
arcpy.RefreshActiveView
df.zoomToSelectedFeatures()
del mxd
