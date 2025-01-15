import arcpy, os
#Get current ArcGIS project and map
CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps()[0]
arcpy.AddMessage("{0}".format(Maps))

Layers = Maps.listlayers("CHS Raster Chart")[0]
TargetGroupLayer = Maps.listlayers("Charts")[0]

Extent = PROE
PolygonPoints = [Extent.lowerLeft, Extent.lowerRight, Extent.upperRight, Extent.upperLeft]
PolygonFeature = arcpy.Polygon(arcpy.Array(PolygonPoints))

arcpy.management.SelectLayerByLocation(Layers, "WITHIN", PolygonFeature, "", "NEW_SELECTION")

ChartFolder = os.listdir("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/")
with arcpy.da.SearchCursor(Layers, ["CHARTNO"]) as Cursor:
    for row in Cursor:
        chart_file = row[0] + ".KAP"
        if chart_file in ChartFolder:
            # Construct the full path to the chart
            Chart = os.path.join("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts", chart_file)
            # Add the chart layer to the group
            new_chart_layer = arcpy.mp.LayerFile(Chart)
            Maps.addLayer(TargetGroupLayer, new_chart_layer)

arcpy.management.SelectLayerByAttribute(Layers,"CLEAR_SELECTION")

SymbologyLayer = "Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/Chart_Symbology.lyr"
for layer in TargetGroupLayer.listLayers():
    arcpy.management.ApplySymbologyFromLayer(layer, SymbologyLayer)