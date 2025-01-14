"""Import arcsys module."""
import arcpy

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps()[0]
Layers = Maps.listlayers()
for layer in Layers:
    if layer.supports("CHARTS"):
        Layers.removeLayer(layer)

mapView = Maps.defaultView
mapView.camera.scale = mapView.camera.scale + 0.05