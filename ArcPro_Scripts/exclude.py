import arcpy

# Get current ArcGIS project and map
CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps()[0]

# This loop will go through all layers
for layer in Maps.listLayers():
    try:
        if layer.isRasterLayer:
            arcpy.AddMessage("###############################################")
            arcpy.AddMessage("## There are charts in the Table of Contents ##")
            arcpy.AddMessage("###############################################")
        elif layer.isGroupLayer == False:
            if layer.isFeatureLayer:
                if layer.supports("name"):
                    arcpy.AddMessage(f"Processing layer: {layer.name}")
                    if layer.supports("DEFINITIONQUERY"):
                        arcpy.management.SelectLayerByAttribute(layer, "SUBSET_SELECTION", "OBJECTID IS NOT NULL")
                        desc = arcpy.Describe(layer)
                        selectedFids = desc.FIDSet
                        if selectedFids:
                            queryList = selectedFids.replace(';', ',')
                            oidFieldName = arcpy.Describe(layer).oidFieldName
                            layer.definitionQuery = '{0} IN ({1})'.format(arcpy.AddFieldDelimiters(layer, oidFieldName), queryList)
                    else:
                        arcpy.AddMessage(f"Layer {layer.name} does not support DEFINITIONQUERY")
            else:
                arcpy.AddMessage(f"Layer {layer.name} is not a feature layer")
    except AttributeError as e:
        arcpy.AddMessage(f"Layer does not support the attribute: {e}")
