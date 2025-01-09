
# Script name: Exclude.py
# Date: Mar 19,2013
# Created by Babak Kasraei
# Description: This tool will work exactly like exclude unselected features in ArcMap 10.1
# Edited by S.Yee 20120321, edited again by S.Bartnik 20140129

import sys,os,math,string,arcpy
from arcpy import env

# Read from current map
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Data Themes")[0]
layer = arcpy.mapping.ListLayers(mxd, "*", df )
# This loop will go through all layers
for lyr in layer:
   if lyr.isRasterLayer == True:
      arcpy.AddMessage("###############################################")
      arcpy.AddMessage("## There are charts in the Table of Contents ##")
      arcpy.AddMessage("###############################################")
   elif lyr.isGroupLayer == False:
      # Tool works only with feature layers.
      if lyr.isFeatureLayer == True:
	 #Filters out layers that do not have the workspace path property (unlikely we'd be excluding features on them anyway)
         if lyr.supports("WORKSPACEPATH"):
            #Finds the workspace path for the layer/Feature Class
            WP = lyr.workspacePath 
            #Creates a describe object for the workspace path
            desWP = arcpy.Describe(WP)
            #Pulls the workspace product type
            WPtype = desWP.workspaceFactoryProgID
         # describe the feature layer to access the the selected set
         desc = arcpy.Describe(lyr)
         # FIDSet will contain the selected features
         selectedFids = desc.FIDSet         
         # If there are selectedFids (a selection set), write them to a new feature
         # class in the current workspace.
         if len(selectedFids) > 0:
             queryList = selectedFids.replace(';', ',')
             # This command finds the ID field name
             oidFieldName = arcpy.Describe(lyr).oidFieldName             
             # This portion was added as Personal Geodatabase SQL syntax is different than the File GDBs or Shapefiles syntax
             if WPtype == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":  #Identifies File Geodatabase
                lyr.definitionQuery =  '{0} in ({1})'. format(arcpy.AddFieldDelimiters(lyr, oidFieldName), queryList)
                arcpy.RefreshActiveView()
             elif WPtype == "esriDataSourcesGDB.AccessWorkspaceFactory.1": #Identifies Personal Geodatabase
                lyr.definitionQuery =  '[{0}] in ({1})'. format(arcpy.AddFieldDelimiters(lyr, oidFieldName), queryList).replace("\"","",2)
                arcpy.RefreshActiveView()
             elif WPtype == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)
                lyr.definitionQuery =  '{0} in ({1})'. format(arcpy.AddFieldDelimiters(lyr, oidFieldName), queryList).replace("\"","",2)      
                arcpy.RefreshActiveView()
             else: #Identifies other types of data file (Shapefiles)
                lyr.definitionQuery =  '{0} in ({1})'. format(arcpy.AddFieldDelimiters(lyr, oidFieldName), queryList)
                arcpy.RefreshActiveView()