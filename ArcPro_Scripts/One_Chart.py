import arcpy, os

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps("Data Themes")[0]
Layers = Maps.listlayers("CHS Raster Chart")[0]
TargetGroupLayer = Maps.listlayers("Charts")[0]
Legend = Maps.listElements("LEGEND_ELEMENT", "Legend")[0]
PolygonFeature = arcpy.Polygon([Maps.extent.lowerLeft, Maps.extent.lowerRight, Maps.extent.upperLeft, Maps.extent.upperRight])
arcpy.management.SelectLayerByLocation(Layers, "WITHIN", PolygonFeature, "", "NEW_SELECTION")
ChartFolder = os.listdir("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/")
Cursor = arcpy.da.SearchCursor(Layers)
FeatureList = []
for row in Cursor:
    FeatureList.append(row.CHARTSCALE)
MaximumScale = max(FeatureList)
Cursor = arcpy.da.SearchCursor(Layers)
for row in Cursor:
    for file in ChartFolder:
        if row.CHARTSCALE == MaximumScale:
            Chart = os.path.join("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/", row.CHARTNO+".KAP" )
Maps.mp.addLayerToGroup(TargetGroupLayer, Chart, "TOP")
arcpy.management.SelectLayerByAttribute(Layers,"CLEAR_SELECTION")
SymbologyLayer = "Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/Chart_Symbology.lyr"
for layer in TargetGroupLayer:
    arcpy.management.ApplySymbologyFromLayer(layer, SymbologyLayer)