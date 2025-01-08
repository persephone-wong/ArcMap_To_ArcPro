import arcpy

CurrentProject = arcpy.mp.ArcGISProject('current')
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
                newName = arcpy.AddFieldDelimiters(layer, "FID")
                layer.definitionQuery =  "".format(newName, queryList)
