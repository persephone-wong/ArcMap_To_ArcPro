import arcpy

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps("Data Themes")[0]
Filters = arcpy.GetParameter(0)
queryList = "','".join(Filters)
LayerList = arcpy.GetParameter(1)

if len(Filters) > 0:
    for layer in Maps.listLayers():
        if layer.name == "Sectors":
            layer.definitionQuery = '"SECTOR" in (\'{0}\')' .format(queryList.upper())

for layer in LayerList:
    if layer.isFeatureLayer:
        arcpy.AddMessage("Now selecting features from: " + layer.name)
        arcpy.management.SelectLayerByLocation(layer.name,"WITHIN",'Sectors')

del CurrentProject