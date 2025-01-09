"""Import arcsys module."""
import arcpy

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps("Data Themes")[0]
Layers = Maps.listlayers()
for layer in Layers:
    if layer.supports("CHARTS"):
        Layers.removeLayer(layer)

##Refreshes Active view    
CurrentProject.activeView.camera.scale = CurrentProject.camera.scale + 0.05