import arcpy

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps("Data Themes")[0]

Layer = arcpy.GetParameter(0)

for layer in arcpy.mp.ListLayers(CurrentProject):
    if layer.name == Layer.name:
        if layer.supports("WORKSPACEPATH"):
                            WorkspacePath = layer.workspacePath
                            DescribeWorkspacePath = arcpy.Describe(WorkspacePath)
                            WorkspacePathType = DescribeWorkspacePath.workspaceFactoryProgID
        if WorkspacePathType == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1" or WorkspacePathType == "esriDataSourcesGDB.AccessWorkspaceFactory.1" or WorkspacePathType == "esriDataSourcesGDB.AccessWorkspaceFactory.1" or WorkspacePathType == "esriDataSourcesGDB.SdeWorkspaceFactory.1":
            layer.definitionQuery = ''
        else:
            layer.definitionQuery = ''
               
arcpy.AddWarning("#########################################################")
arcpy.AddWarning("###                       SUCCESS                     ###")
arcpy.AddWarning("###        Classification Combine Tool Finished       ###")
arcpy.AddWarning("#########################################################")
del CurrentProject