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
            if lyr.supports("WORKSPACEPATH"):