import arcpy

CurrentProject = arcpy.mp.ArcGISProject('current')
Maps = CurrentProject.listMaps()[0]

SelectedLayer = [Maps.listLayers.lyr.getSelectionSet()]
WorkspacePathType = None

for layer in arcpy.mp.ListLayers(CurrentProject):
    if layer.getDefinition("V3").serviceLayerID in SelectedLayer:
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