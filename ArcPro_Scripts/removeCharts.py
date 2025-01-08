"""Import arcsys module."""
import arcpy

CurrentProject = arcpy.mp.ArcGISProject('current')
Maps = CurrentProject.listMaps("Data Themes")[0]
Layers = Maps.listlayers()
for layer in Layers:
    if layer.supports("CHARTS"):
        Layers.removeLayer()

##Refreshes Active view    
CurrentProject.activeView.camera.scale = CurrentProject.camera.scale + 0.05