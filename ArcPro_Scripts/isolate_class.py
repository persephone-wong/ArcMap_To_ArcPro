import arcpy
from time import sleep

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps("Data Themes")[0]

for layer in arcpy.mp.ListLayers(CurrentProject):
    if layer.name == "Approved Areas":
        if layer.supports("WORKSPACEPATH"):
            WorkspacePath = layer.workspacePath
            DescribeWorkspacePath = arcpy.Describe(WorkspacePath)
            WorkspacePathType = DescribeWorkspacePath.workspaceFactoryProgID
            
            if WorkspacePathType == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":
                layer.definitionQuery = '"class_code" Like \'A\''
            elif WorkspacePathType == "esriDataSourcesGDB.AccessWorkspaceFactory.1":
                layer.definitionQuery = '[class_code] Like \'A\''
            elif WorkspacePathType == "esriDataSourcesGDB.SdeWorkspaceFactory.1":
                layer.definitionQuery ='class_code Like \'A\''
            else: 
                layer.definitionQuery = '"class_code" Like \'A\''

    elif layer.name == "Restricted Areas":
        if layer.supports("WORKSPACEPATH"):
            WorkspacePath = layer.workspacePath
            DescribeWorkspacePath = arcpy.Describe(WorkspacePath)
            WorkspacePathType = DescribeWorkspacePath.workspaceFactoryProgID
        
            if WorkspacePathType == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":
                layer.definitionQuery = '"class_code" Like \'R\''
            elif WorkspacePathType == "esriDataSourcesGDB.AccessWorkspaceFactory.1":
                layer.defintionQuery = layer.definitionQuery = '[class_code] Like \'R\''
            elif WorkspacePathType == "esriDataSourcesGDB.SdeWorkspaceFactory.1":
                layer.defintionQuery = 'class_code Like \'R\'' 
            else: 
                layer.defintionQuery = 'class_code Like \'R\'' 
    
    elif layer.name == "Prohibited Areas":
        if layer.supports("WORKSPACEPATH"):
            WorkspacePath = layer.workspacePath
            DescribeWorkspacePath = arcpy.Describe(WorkspacePath)
            WorkspacePathType = DescribeWorkspacePath.workspaceFactoryProgID
            if WorkspacePathType == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":
                layer.definitionQuery = '"class_code" Like \'P\''
            elif WorkspacePathType == "esriDataSourcesGDB.AccessWorkspaceFactory.1":
                layer.defintionQuery = layer.definitionQuery = '[class_code] Like \'P\''
            elif WorkspacePathType == "esriDataSourcesGDB.SdeWorkspaceFactory.1":
                layer.defintionQuery = 'class_code Like \'P\'' 
            else: 
                layer.defintionQuery = 'class_code Like \'P\'' 
    
    elif layer.name == "Marine Sample Site":
        if layer.supports("WORKSPACEPATH"):
            WorkspacePath = layer.workspacePath
            DescribeWorkspacePath = arcpy.Describe(WorkspacePath)
            WorkspacePathType = DescribeWorkspacePath.workspaceFactoryProgID
            if WorkspacePathType == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":
                layer.definitionQuery = '"SS_STATUS" Like \'active\''
            elif WorkspacePathType == "esriDataSourcesGDB.AccessWorkspaceFactory.1":
                layer.defintionQuery = layer.definitionQuery = '[SS_STATUS] Like \'active\'' 
            elif WorkspacePathType == "esriDataSourcesGDB.SdeWorkspaceFactory.1":
                layer.defintionQuery = 'SS_STATUS Like \'active\'' 
            else: 
                layer.defintionQuery = '"SS_STATUS" Like \'active\''

    elif layer.name == "Inactive Marine Site":
        if layer.supports("WORKSPACEPATH"):
            WorkspacePath = layer.workspacePath
            DescribeWorkspacePath = arcpy.Describe(WorkspacePath)
            WorkspacePathType = DescribeWorkspacePath.workspaceFactoryProgID
            if WorkspacePathType == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":
                layer.definitionQuery = '"SS_STATUS" Like \'inactive\'' 
            elif WorkspacePathType == "esriDataSourcesGDB.AccessWorkspaceFactory.1":
                layer.defintionQuery = layer.definitionQuery = '[SS_STATUS] Like \'inactive\''
            elif WorkspacePathType == "esriDataSourcesGDB.SdeWorkspaceFactory.1":
                layer.defintionQuery = 'SS_STATUS Like \'inactive\''
            else: 
                layer.defintionQuery = '"SS_STATUS" Like \'inactive\''
arcpy.AddWarning("###############################################")
arcpy.AddWarning("###                  SUCCESS                ###")
arcpy.AddWarning("###           Isolate Tool Finished         ###")
arcpy.AddWarning("###############################################")
sleep(2)
del CurrentProject