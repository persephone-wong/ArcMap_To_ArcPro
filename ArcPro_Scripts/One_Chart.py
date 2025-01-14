import arcpy, os

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps()[0]
MapLayouts = CurrentProject.listLayouts()[0]
Layers = Maps.listLayers("CHS Raster Chart")[0]
TargetGroupLayer = Maps.listLayers("Charts")[0]
Legend = MapLayouts.listElements("LEGEND_ELEMENT", "Legend")[0]
Extent = Maps.extent
PolygonPoints = [Extent.lowerLeft, Extent.lowerRight, Extent.upperRight, Extent.upperLeft]
PolygonFeature = arcpy.Polygon(arcpy.Array(PolygonPoints))

arcpy.management.SelectLayerByLocation(Layers, "WITHIN", PolygonFeature, "", "NEW_SELECTION")

ChartFolder = os.listdir("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/")
Cursor = arcpy.da.SearchCursor(Layers)
FeatureList = []
with arcpy.da.SearchCursor(Layers, ["CHARTSCALE", "CHARTNO"]) as Cursor:
    for row in Cursor:
        FeatureList.append(row[0])  # row[0] is CHARTSCALE

MaximumScale = max(FeatureList)
with arcpy.da.SearchCursor(Layers, ["CHARTSCALE", "CHARTNO"]) as Cursor:
    for row in Cursor:
        if row[0] == MaximumScale:
            # Construct the path to the chart
            Chart = os.path.join("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/", row[1] + ".KAP")
            # Add the chart as a layer to the map and group layer
            new_chart_layer = arcpy.mp.LayerFile(Chart)
            Maps.addLayer(TargetGroupLayer, new_chart_layer)

Maps.mp.addLayerToGroup(TargetGroupLayer, Chart, "TOP")
arcpy.management.SelectLayerByAttribute(Layers,"CLEAR_SELECTION")
SymbologyLayer = "Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/Chart_Symbology.lyr"
for layer in TargetGroupLayer.listLayers():
    arcpy.management.ApplySymbologyFromLayer(layer, SymbologyLayer)
