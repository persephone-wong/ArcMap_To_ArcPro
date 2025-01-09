import arcpy, os

CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps("Data Themes")[0]
Layers = Maps.listlayers("CHS Raster Chart")[0]
TargetGroupLayer = Maps.listlayers("Charts")[0]
try: 
    Legend = (CurrentProject.listLayouts*('Layout')[0]).listElements('LEGEND_ELEMENT')
except:
    arcpy.AddMessage("No Legend in Layout View")
PolygonFeature = arcpy.Polygon([Maps.extent.lowerLeft, Maps.extent.lowerRight, Maps.extent.upperLeft, Maps.extent.upperRight])
arcpy.management.SelectLayerByLocation(Layers, "CONTAINS", PolygonFeature, "", "NEW_SELECTION")
Cursor = arcpy.da.SearchCursor(Layers)
FeatureList = []
for row in Cursor:
    FeatureList.append(row.CHARTSCALE)
MaximumScale = min(FeatureList)
ChartFolder = os.listdir("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/")

for row in Cursor:
    for file in ChartFolder:
        if row.CHARTSCALE == MaximumScale:
            Chart = os.path.join("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/", row.CHARTNO+".KAP")

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

for layer in TargetGroupLayer:
    arcpy.management.ApplySymbologyFromLayer(layer, SymbologyLayer)
