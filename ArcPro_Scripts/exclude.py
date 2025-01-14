import arcpy

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps()[0]

for layer in Maps.listLayers():
    if layer.isRasterLayer:
        arcpy.AddMessage("##########################################")
        arcpy.AddMessage("## There are charts in table of content ##")
        arcpy.AddMessage("##########################################")
    elif layer.isGroupLayer:
        for subLayer in layer.listLayers():
            if subLayer.isFeatureLayer:
                if subLayer.supports("WORKSPACEPATH"):
                    WorkspacePath = subLayer.workspacePath
                    DescribeWorkspacePath = arcpy.Describe(WorkspacePath)
                    WorkspacePathType = DescribeWorkspacePath.workspaceFactoryProgID
                else:
                    continue
                DescribeLayer = arcpy.Describe(subLayer)
                SelectedFids = DescribeLayer.FIDSet
                
                if len(SelectedFids) > 0:
                    QueryList = SelectedFids.replace(';', ',')
                    OidFieldName = arcpy.Describe(subLayer).OIDFieldName
                    if WorkspacePath == "esriDataSourcesGDB.FileGDBWorkspaceFactory.1":
                        subLayer.definitionQuery = '{0} in ({1})'.format(arcpy.AddFieldDelimiters(subLayer, OidFieldName, QueryList))
                    elif WorkspacePath == "esriDataSourcesGDB.AccessWorkspaceFactory.1":
                        subLayer.definitionQuery =  '[{0}] in ({1})'. format(arcpy.AddFieldDelimiters(subLayer, OidFieldName), QueryList).replace("\"","",2)
                    elif WorkspacePath == "esriDataSourcesGDB.SdeWorkspaceFactory.1": #Identifies SDE database (MWQM does not use them so this code might not work properly if actually applied)
                        subLayer.definitionQuery =  '{0} in ({1})'. format(arcpy.AddFieldDelimiters(subLayer, OidFieldName), QueryList).replace("\"","",2)      
                    else: #Identifies other types of data file (Shapefiles)
                        subLayer.definitionQuery =  '{0} in ({1})'. format(arcpy.AddFieldDelimiters(subLayer, OidFieldName), QueryList)
