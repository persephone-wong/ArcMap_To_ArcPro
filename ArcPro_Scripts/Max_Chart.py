import arcpy, os

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps()[0]
Layers = Maps.listlayers("CHS Raster Chart")[0]
TargetGroupLayer = Maps.listlayers("Charts")[0]
try: 
    Legend = (CurrentProject.listLayouts*('Layout')[0]).listElements('LEGEND_ELEMENT')[0]
except:
    arcpy.AddMessage("No Legend in Layout View")


Extent = Maps.extent
PolygonPoints = [Extent.lowerLeft, Extent.lowerRight, Extent.upperRight, Extent.upperLeft]
PolygonFeature = arcpy.Polygon(arcpy.Array(PolygonPoints))


arcpy.management.SelectLayerByLocation(Layers, "CONTAINS", PolygonFeature, "", "NEW_SELECTION")
FeatureList = []
with arcpy.da.SearchCursor(Layers, ["CHARTSCALE", "CHARTNO"]) as Cursor:
    for row in Cursor:
        FeatureList.append(row[0])  # row[0] is CHARTSCALE

MaximumScale = min(FeatureList)

ChartFolder = os.listdir("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/")

with arcpy.da.SearchCursor(Layers, ["CHARTSCALE", "CHARTNO"]) as Cursor:
    for row in Cursor:
        if row[0] == MaximumScale:
            # Construct the full path to the chart
            Chart = os.path.join("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/", row[1] + ".KAP")
            # Add the chart layer to the group
            new_chart_layer = arcpy.mp.LayerFile(Chart)
            Maps.addLayer(TargetGroupLayer, new_chart_layer)

SymbologyLayer = "Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/Chart_Symbology.lyr"
"""
try:
   legend.autoAdd = False
except:
    arcpy.AddMessage("No Legend in Layout View")
    Not Ported Over.
    """
Maps.mp.addLayerToGroup(TargetGroupLayer, Chart, "TOP")
arcpy.management.ApplySymbologyFromLayer(Chart, SymbologyLayer)
arcpy.management.SelectLayerByAttribute_management(Layers,"CLEAR_SELECTION")

for layer in TargetGroupLayer.listLayers():
    arcpy.management.ApplySymbologyFromLayer(layer, SymbologyLayer)

