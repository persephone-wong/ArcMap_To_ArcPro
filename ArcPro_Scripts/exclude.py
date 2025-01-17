import arcpy

# Get current ArcGIS project and map
CurrentProject = arcpy.mp.ArcGISProject('CURRENT')
Maps = CurrentProject.listMaps()[0]

# This loop will go through all layers
for lyr in Maps.listLayers():
    if lyr.isRasterLayer:
        arcpy.AddMessage("###############################################")
        arcpy.AddMessage("## There are charts in the Table of Contents ##")
        arcpy.AddMessage("###############################################")
    elif not lyr.isGroupLayer:
        # Tool works only with feature layers.
        if lyr.isFeatureLayer:
            arcpy.AddMessage(f"Processing layer: {lyr.name}")
            # Check if the layer supports DEFINITIONQUERY
            if lyr.supports("DEFINITIONQUERY"):
                # Describe the feature layer to access the selected set
                desc = arcpy.Describe(lyr)
                # FIDSet will contain the selected features
                selectedFids = desc.FIDSet
                arcpy.AddMessage(f"Selected FIDs: {selectedFids}")
                # If there are selectedFids (a selection set), write them to a new feature class in the current workspace.
                if selectedFids:
                    queryList = selectedFids.replace(';', ',')
                    # This command finds the ID field name
                    oidFieldName = arcpy.Describe(lyr).oidFieldName
                    arcpy.AddMessage(f"OID Field Name: {oidFieldName}")
                    # Apply the definition query to show only the selected features
                    lyr.definitionQuery = '{0} IN ({1})'.format(arcpy.AddFieldDelimiters(lyr, oidFieldName), queryList)
                    arcpy.AddMessage(f"Definition Query set to: {lyr.definitionQuery}")
            else:
                arcpy.AddMessage(f"Layer {lyr.name} does not support DEFINITIONQUERY")
        else:
            arcpy.AddMessage(f"Layer {lyr.name} is not a feature layer")

# Refresh the active view
arcpy.RefreshActiveView()
arcpy.AddMessage("Active view refreshed")