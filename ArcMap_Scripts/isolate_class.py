# ---------------------------------------------------------------------------
# isolate_class.py
# Created on: 2015-09-11 based on selectbysector_rev.py
# Created by: Sarah Bartnik  
# Description: 
# This script will isolate each classification in the classification.gdb &
# write the appropriate SQL query in the definition query box, so our
# exclude tool works properly.
# ---------------------------------------------------------------------------

# Import arcpy and python modules
import sys,os,math,string,arcpy,time
from arcpy import env

# Script arguments
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Data Themes")[0]

# Puts the parameter string and the field string in the definition query box for the Sectors feature
for lyr in arcpy.mapping.ListLayers(mxd):
    #Does Approved Areas layer definition query
    if lyr.name == "Approved Areas":
        #Filters out layers that do not have the workspace path property (unlikely we'd be excluding features on them anyway)
        if lyr.supports("WORKSPACEPATH"):
            #Finds the workspace path for the layer/Feature Class
            WP = lyr.workspacePath 
            #Creates a describe object for the workspace path
            desWP = arcpy.Describe(WP)
            #Pulls the workspace product type
            WPtype = desWP.workspaceFactoryProgID
            
        if WPtype == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":  #Identifies File Geodatabase
            lyr.definitionQuery = '"class_code" Like \'A\'' 
        elif WPtype == "esriDataSourcesGDB.AccessWorkspaceFactory.1": #Identifies Personal Geodatabase
            lyr.definitionQuery = '[class_code] Like \'A\'' 
        elif WPtype == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)            
            lyr.definitionQuery = 'class_code Like \'A\'' 
        else: #Identifies other types of data file (Shapefiles)
            lyr.definitionQuery = '"class_code" Like \'A\''             

    #Does Approved Area (Harvest Type) layer definition query
    if lyr.name == "Approved Harvest Type":
        #Filters out layers that do not have the workspace path property (unlikely we'd be excluding features on them anyway)
        if lyr.supports("WORKSPACEPATH"):
            #Finds the workspace path for the layer/Feature Class
            WP = lyr.workspacePath 
            #Creates a describe object for the workspace path
            desWP = arcpy.Describe(WP)
            #Pulls the workspace product type
            WPtype = desWP.workspaceFactoryProgID
            
        if WPtype == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":  #Identifies File Geodatabase
            lyr.definitionQuery = '"class_code" Like \'A\'' 
        elif WPtype == "esriDataSourcesGDB.AccessWorkspaceFactory.1": #Identifies Personal Geodatabase
            lyr.definitionQuery = '[class_code] Like \'A\'' 
        elif WPtype == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)            
            lyr.definitionQuery = 'class_code Like \'A\'' 
        else: #Identifies other types of data file (Shapefiles)
            lyr.definitionQuery = '"class_code" Like \'A\''

    #Does Conditional Areas layer definition query
    if lyr.name == "Conditional Areas":
        #Filters out layers that do not have the workspace path property (unlikely we'd be excluding features on them anyway)
        if lyr.supports("WORKSPACEPATH"):
            #Finds the workspace path for the layer/Feature Class
            WP = lyr.workspacePath 
            #Creates a describe object for the workspace path
            desWP = arcpy.Describe(WP)
            #Pulls the workspace product type
            WPtype = desWP.workspaceFactoryProgID
            
        if WPtype == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":  #Identifies File Geodatabase
            lyr.definitionQuery = '"class_code" in (\'CA\',\'CR\')' 
        elif WPtype == "esriDataSourcesGDB.AccessWorkspaceFactory.1": #Identifies Personal Geodatabase
            lyr.definitionQuery = '[class_code] in (\'CA\',\'CR\')' 
        elif WPtype == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)            
            lyr.definitionQuery = 'class_code in (\'CA\',\'CR\')' 
        else: #Identifies other types of data file (Shapefiles)
            lyr.definitionQuery = '"class_code" in (\'CA\',\'CR\')'
            
    #Does Restricted Areas layer definition query
    if lyr.name == "Restricted Areas":
        #Filters out layers that do not have the workspace path property (unlikely we'd be excluding features on them anyway)
        if lyr.supports("WORKSPACEPATH"):
            #Finds the workspace path for the layer/Feature Class
            WP = lyr.workspacePath 
            #Creates a describe object for the workspace path
            desWP = arcpy.Describe(WP)
            #Pulls the workspace product type
            WPtype = desWP.workspaceFactoryProgID
            
        if WPtype == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":  #Identifies File Geodatabase
            lyr.definitionQuery = '"class_code" Like \'R\'' 
        elif WPtype == "esriDataSourcesGDB.AccessWorkspaceFactory.1": #Identifies Personal Geodatabase
            lyr.definitionQuery = '[class_code] Like \'R\'' 
        elif WPtype == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)            
            lyr.definitionQuery = 'class_code Like \'R\'' 
        else: #Identifies other types of data file (Shapefiles)
            lyr.definitionQuery = '"class_code" Like \'R\''

    #Does Prohibited Areas layer definition query
    if lyr.name == "Prohibited Areas":
        #Filters out layers that do not have the workspace path property (unlikely we'd be excluding features on them anyway)
        if lyr.supports("WORKSPACEPATH"):
            #Finds the workspace path for the layer/Feature Class
            WP = lyr.workspacePath 
            #Creates a describe object for the workspace path
            desWP = arcpy.Describe(WP)
            #Pulls the workspace product type
            WPtype = desWP.workspaceFactoryProgID
            
        if WPtype == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":  #Identifies File Geodatabase
            lyr.definitionQuery = '"class_code" Like \'P\'' 
        elif WPtype == "esriDataSourcesGDB.AccessWorkspaceFactory.1": #Identifies Personal Geodatabase
            lyr.definitionQuery = '[class_code] Like \'P\'' 
        elif WPtype == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)            
            lyr.definitionQuery = 'class_code Like \'P\'' 
        else: #Identifies other types of data file (Shapefiles)
            lyr.definitionQuery = '"class_code" Like \'P\''

 #Does Marine Sample Sites layer definition query
    if lyr.name == "Marine Sample Site":
        #Filters out layers that do not have the workspace path property (unlikely we'd be excluding features on them anyway)
        if lyr.supports("WORKSPACEPATH"):
            #Finds the workspace path for the layer/Feature Class
            WP = lyr.workspacePath 
            #Creates a describe object for the workspace path
            desWP = arcpy.Describe(WP)
            #Pulls the workspace product type
            WPtype = desWP.workspaceFactoryProgID
            
        if WPtype == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":  #Identifies File Geodatabase
            lyr.definitionQuery = '"SS_STATUS" Like \'active\'' 
        elif WPtype == "esriDataSourcesGDB.AccessWorkspaceFactory.1": #Identifies Personal Geodatabase
            lyr.definitionQuery = '[SS_STATUS] Like \'active\'' 
        elif WPtype == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)            
            lyr.definitionQuery = 'SS_STATUS Like \'active\'' 
        else: #Identifies other types of data file (Shapefiles)
            lyr.definitionQuery = '"SS_STATUS" Like \'active\''

 #Does Inactive Marine Sample Sites layer definition query
    if lyr.name == "Inactive Marine Site":
        #Filters out layers that do not have the workspace path property (unlikely we'd be excluding features on them anyway)
        if lyr.supports("WORKSPACEPATH"):
            #Finds the workspace path for the layer/Feature Class
            WP = lyr.workspacePath 
            #Creates a describe object for the workspace path
            desWP = arcpy.Describe(WP)
            #Pulls the workspace product type
            WPtype = desWP.workspaceFactoryProgID
            
        if WPtype == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":  #Identifies File Geodatabase
            lyr.definitionQuery = '"SS_STATUS" Like \'inactive\'' 
        elif WPtype == "esriDataSourcesGDB.AccessWorkspaceFactory.1": #Identifies Personal Geodatabase
            lyr.definitionQuery = '[SS_STATUS] Like \'inactive\'' 
        elif WPtype == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)            
            lyr.definitionQuery = 'SS_STATUS Like \'inactive\'' 
        else: #Identifies other types of data file (Shapefiles)
            lyr.definitionQuery = '"SS_STATUS" Like \'inactive\''



arcpy.AddWarning("###############################################")
arcpy.AddWarning("###                  SUCCESS                ###")
arcpy.AddWarning("###           Isolate Tool Finished         ###")
arcpy.AddWarning("###############################################")
time.sleep(2)

#Refresh the screen and zoom to the selected features
arcpy.RefreshActiveView
del mxd




