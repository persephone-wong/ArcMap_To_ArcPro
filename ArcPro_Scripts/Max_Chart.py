import arcpy, os
#Get current ArcGIS project and map
CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps()[0]
Layout = CurrentProject.listLayouts()[0]

arcpy.AddMessage("{0}".format(Maps))

Layers = Maps.listLayers("CHS Raster Chart")[0]
TargetGroupLayer = Maps.listLayers("Charts")[0]
try:
    legend = [element for element in Layout.listElements("LEGEND_ELEMENT") if element.name == "Legend"][0]
except IndexError:
    arcpy.AddMessage("No Legend in Layout View")

Extent = CurrentProject.activeMap.defaultView.camera.getExtent()
PolygonPoints = [Extent.lowerLeft, Extent.lowerRight, Extent.upperRight, Extent.upperLeft]
PolygonFeature = arcpy.Polygon(arcpy.Array(PolygonPoints))

arcpy.management.SelectLayerByLocation(Layers, "CONTAINS", PolygonFeature, "", "NEW_SELECTION")

featureList = []
for row in arcpy.da.SearchCursor(Layers, ["CHARTSCALE"]):
    featureList.append(row[0])
MX = min(featureList)
ChartFolder = os.listdir("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/")
Chart = None

with arcpy.da.SearchCursor(Layers, ["CHARTSCALE", "CHARTNO"]) as Cursor:
    for row in Cursor:
        if row[0] == MX:
            Chart_file = row[1] + ".KAP"
            if Chart_file in ChartFolder:
                Chart = os.path.join("Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/", Chart_file)
                break

if Chart:
    result = arcpy.MakeRasterLayer_management(Chart, "raster_layer")
    addLayer = result.getOutput(0)
    Maps.addLayerToGroup(TargetGroupLayer, addLayer, "TOP")
arcpy.management.SelectLayerByAttribute(Layers,"CLEAR_SELECTION")

SymbologyLayer = "Q:/GW/EC1210WQAEH_QESEA/CSSP_PYR/SDMRS2/Charts/Chart_Symbology.lyr"
for layer in TargetGroupLayer.listLayers():
    arcpy.management.ApplySymbologyFromLayer(layer, SymbologyLayer)