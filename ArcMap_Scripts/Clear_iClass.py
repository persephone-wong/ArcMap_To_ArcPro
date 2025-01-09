# ---------------------------------------------------------------------------
# clear_iclass.py
# Created on: 2015-12-02 based on isolate_class.py
# Created by: Sarah Bartnik  
# Description: 
# This script will delete definitions queries in classification layers that are inputs to the
# SSC Table model. This tool will make sure the modified SSC Table tool works properly.
# ---------------------------------------------------------------------------

# Import arcpy and python modules
import sys,os,math,string,arcpy,time
from arcpy import env

# Script arguments
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Data Themes")[0]

# Collects layer name from user and sends it to script
getLayer = arcpy.GetParameter(0)

for lyr in arcpy.mapping.ListLayers(mxd, "*", df):
    
    #Changes definition query of selected layer
    if lyr.name == getLayer.name:
        #Filters out layers that do not have the workspace path property (unlikely we'd be excluding features on them anyway)
        if lyr.supports("WORKSPACEPATH"):
            #Finds the workspace path for the layer/Feature Class
            WP = lyr.workspacePath 
            #Creates a describe object for the workspace path
            desWP = arcpy.Describe(WP)
            #Pulls the workspace product type
            WPtype = desWP.workspaceFactoryProgID
            
        if WPtype == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":  #Identifies File Geodatabase
           lyr.definitionQuery = '' 
        elif WPtype == "esriDataSourcesGDB.AccessWorkspaceFactory.1": #Identifies Personal Geodatabase
            lyr.definitionQuery = '' 
        elif WPtype == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)            
            lyr.definitionQuery = '' 
        else: #Identifies other types of data file (Shapefiles)
            lyr.definitionQuery = ''

arcpy.AddWarning("#########################################################")
arcpy.AddWarning("###                       SUCCESS                     ###")
arcpy.AddWarning("###        Classification Combine Tool Finished       ###")
arcpy.AddWarning("#########################################################")

del mxd
