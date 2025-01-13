import arcpy

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps("Data Themes")[0]
Filters = arcpy.GetParameter(0)
if Filters:
    queryList = "','".join(Filters)
    queryString = '"SECTOR" in (\'{0}\')'.format(queryList)

    for layer in Maps.listLayers():
        if layer.name == "Sectors":
            layer.definitionQuery = queryString

LayerList = arcpy.GetParameter(1)

if LayerList:
    for layer in LayerList:
        if layer.isFeatureLayer:
            arcpy.AddMessage(f"Now selecting features from: {layer.name}")
            # Apply the spatial selection based on "Sectors" layer
            arcpy.management.SelectLayerByLocation(layer, "WITHIN", "Sectors")

del CurrentProject