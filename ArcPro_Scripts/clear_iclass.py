import arcpy

CurrentProject = arcpy.mp.ArcGISProject('current')
Maps = CurrentProject.listMaps()[0]

SelectedLayers = [layer for layer in Maps.listLayers() if layer.isFeatureLayer and layer.getSelectionSet()]
WorkspacePathType = None

for layer in SelectedLayers:
    if layer.supports("WORKSPACEPATH"):
        WorkspacePath = layer.workspacePath
        DescribeWorkspacePath = arcpy.Describe(WorkspacePath)
        WorkspacePathType = DescribeWorkspacePath.workspaceFactoryProgID
    if WorkspacePathType in [
        "esriDataSourcesGDB.FileGDBWorkspaceFactory.1", 
        "esriDataSourcesGDB.AccessWorkspaceFactory.1", 
        "esriDataSourcesGDB.SdeWorkspaceFactory.1"
    ]:            
        layer.definitionQuery = ''
    else:
        layer.definitionQuery = ''

arcpy.AddWarning("#########################################################")
arcpy.AddWarning("###                       SUCCESS                     ###")
arcpy.AddWarning("###        Classification Combine Tool Finished       ###")
arcpy.AddWarning("#########################################################")
del CurrentProject