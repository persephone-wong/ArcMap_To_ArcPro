import arcpy

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps("Data Themes")[0]
Layers = Maps.listlayers()

for layer in Layers:
    if layer.isRasterLayer:
        arcpy.AddMessage("##########################################")
        arcpy.AddMessage("## There are charts in table of content ##")
        arcpy.AddMessage("##########################################")
    elif layer.isGroupLayer == False:
         if layer.isFeatureLayer:
             desc = arcpy.Describe(layer)
             selectedFids = desc.FIDSet
             if len(selectedFids) > 0:
                queryList = selectedFids.replace(';', ',')
                OidFieldName = arcpy.Describe(layer).OIDFieldName
                newName = arcpy.AddFieldDelimiters(layer, OidFieldName)
                layer.definitionQuery = "{} IN ({})".format(newName, queryList)

arcpy.AddMessage("##########################################")
arcpy.AddMessage("### Definition Queries Applied Successfully ###")
arcpy.AddMessage("##########################")