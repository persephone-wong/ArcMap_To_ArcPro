import arcpy

CurrentProject = arcpy.mp.ArcGISProject('current')
Maps = CurrentProject.listMaps()[0]

for layer in Maps.listLayers():
    if layer.isRasterLayer:
        arcpy.AddMessage("##########################################")
        arcpy.AddMessage("## There are charts in table of content ##")
        arcpy.AddMessage("##########################################")
    elif layer.isGroupLayer == False:
         if layer.isFeatureLayer:
             if layer.supports("name"):
                 arcpy.AddMessage(f"Processing layer: {layer.name}")
                 if layer.supports("DEFINITIONQUERY"):
                    arcpy.management.SelectLayerByAttribute(layer, "SUBSET_SELECTION", "OBJECTID IS NOT NULL")
                    desc = arcpy.Describe(layer)
                    selectedFids = desc.FIDSet
                    if len(selectedFids) > 0:
                        queryList = selectedFids.replace(';', ',')
                        OidFieldName = arcpy.Describe(layer).OIDFieldName
                        newName = arcpy.AddFieldDelimiters(layer, OidFieldName)
                        layer.definitionQuery = "".format(newName, queryList)
arcpy.AddMessage("##########################################")
arcpy.AddMessage("### Definition Queries Applied Successfully ###")
arcpy.AddMessage("##########################")