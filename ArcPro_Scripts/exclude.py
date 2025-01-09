import arcpy

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps("Data Themes")[0]
Layers = Maps.listlayers()

for layer in Layers:
    if layer.isRasterLayer:
        arcpy.AddMessage("##########################################")
        arcpy.AddMessage("## There are charts in table of content ##")
        arcpy.AddMessage("##########################################")
    elif layer.isGroupLayer:
        if layer.isFeatureLayer:
            if layer.supports("WORKSPACEPATH"):
                WorkspacePath = layer.workspacePath
                DescribeWorkspacePath = arcpy.Describe(WorkspacePath)
                WorkspacePathType = DescribeWorkspacePath.workspaceFactoryProgID
            DescribeLayer = arcpy.Describe(layer)
            SelectedFids = DescribeLayer.FIDSet
            if len(SelectedFids) > 0:
                QueryList = SelectedFids.replace(';', ',')
                OidFieldName = arcpy.Describe(layer).OIDFieldName
                if WorkspacePath == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":
                    layer.definitionQuery = '{0} in ({1})'.format(arcpy.AddFieldDelimiters(layer, OidFieldName, QueryList))
                elif WorkspacePath == "esriDataSourcesGDB.AccessWorkspaceFactory.1":
                    layer.definitionQuery =  '[{0}] in ({1})'. format(arcpy.AddFieldDelimiters(layer, OidFieldName), QueryList).replace("\"","",2)
                elif WorkspacePath == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)
                    layer.definitionQuery =  '{0} in ({1})'. format(arcpy.AddFieldDelimiters(layer, OidFieldName), QueryList).replace("\"","",2)      
                else: #Identifies other types of data file (Shapefiles)
                    layer.definitionQuery =  '{0} in ({1})'. format(arcpy.AddFieldDelimiters(layer, OidFieldName), QueryList)
