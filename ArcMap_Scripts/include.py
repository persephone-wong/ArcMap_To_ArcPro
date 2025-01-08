
# Script name: Include.py
# Date: Mar 19,2013
# Created by Babak Kasraei
# Description: This tool restore unselected features in ArcMap 10.1


import sys,os,math,string,arcpy
from arcpy import env

# Read from current map
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Data Themes")[0]
layer = arcpy.mapping.ListLayers(mxd, "*", df )

#layer_list = [layer for layer in arcpy.mapping.ListLayers(mxd) if 'FID' in [field.name for field in arcpy.ListFields(layer, 'FID')]]

for lyr in layer:
   if lyr.isRasterLayer == True:
      arcpy.AddMessage("##########################################")
      arcpy.AddMessage("## There are charts in table of content ##")
      arcpy.AddMessage("##########################################")
   elif lyr.isGroupLayer == False:
      if lyr.isFeatureLayer == True:
       # describe the feature layer to access the the selected set
         desc = arcpy.Describe(lyr)
      # FIDSet will contain the selected features
         selectedFids = desc.FIDSet

       # If there are selectedFids (a selection set), write them to a new feature
       # class in the current workspace.
         if len(selectedFids) > 0:
      
            queryList = selectedFids.replace(';', ',')
            newName = arcpy.AddFieldDelimiters(lyr, "FID")
            lyr.definitionQuery =  "" .format(newName, queryList)
            arcpy.RefreshActiveView()	
   

