# ---------------------------------------------------------------------------
# CreateReports.py
# Created on: 2013-04-26 	Modified on: 2016-08-05
# Created by: Sarah Bartnik  
# Description: 
# Process to run a previously created report template with one click
# ---------------------------------------------------------------------------

# Import arcpy and python modules
import arcpy, os, string
import getpass

# Script arguments
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Data Themes")[0]
reportType = arcpy.GetParameterAsText(0)
pdfFilename = arcpy.GetParameterAsText(1)
pdfExtension = "pdf"
xlsExtension = "xls"

# Creates file save location from input parameters
username = getpass.getuser()
pdfDirectory = "\\\int.ec.gc.ca\\PROFILES\\RemoteDesktop\\InGEO2\\" + username + "\\Desktop\\"
arcpy.AddMessage("Saving your file to: " + pdfDirectory)
pdfPath = pdfDirectory + pdfFilename + '.' + pdfExtension
xlsPath = pdfDirectory + pdfFilename + '.' + xlsExtension

#Switch to match up proper report template with input parameter selection
if reportType == "Finfish Tenures":
    layerName = "Finfish Tenures"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_psi_finfish_template.rlf",
                                  pdfPath,"USE_RLF")
        #Returns value so that proper status message can be sent
        successCheck = 1 #value 1 is "ok", 2 is SSC problem, 3 is fail
    else:
        successCheck = 3 #value 1 is "ok", 2 is SSC problem, 3 is fail
elif reportType == "Floathomes":
    layerName = "Floathomes"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:    
        arcpy.mapping.ExportReport(lyr,
                                   r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_psi_floathome_template.rlf",
                                   pdfPath,"USE_RLF")
        #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Marinas and Docks PNW":
    layerName = "Marinas and Docks PNW"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_psi_marinas_template.rlf",
                                  pdfPath,"USE_RLF")
        #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Marine Sample Site - Active":
    layerName = "Marine Sample Site"	
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to only allow active stations to be shown in report
    arcpy.SelectLayerByAttribute_management(lyr,"REMOVE_FROM_SELECTION",""""SS_STATUS" = 'inactive'""")
    arcpy.AddMessage(lyr.definitionQuery)
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_mw_sites_template.rlf",
                                  pdfPath,"USE_RLF")
        #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Marine Sample Site - Inactive":
    layerName = "Inactive Marine Site"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to only allow active stations to be shown in report
    arcpy.SelectLayerByAttribute_management(lyr,"REMOVE_FROM_SELECTION",""""SS_STATUS" = 'active'""")
    arcpy.AddMessage(lyr.definitionQuery)
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_imw_sites_template.rlf",
                                  pdfPath,"USE_RLF")
        #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Freshwater Sample Site - Active":
    layerName = "Freshwater Sample Site"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to only allow active stations to be shown in report
    arcpy.SelectLayerByAttribute_management(lyr,"REMOVE_FROM_SELECTION",""""SS_STATUS" = 'inactive'""")
    arcpy.AddMessage(lyr.definitionQuery)
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_fw_sites_template.rlf",
                                  pdfPath,"USE_RLF")
    #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Freshwater Sample Site - Inactive":
    layerName = "Inactive Freshwater Site"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to only allow active stations to be shown in report
    arcpy.SelectLayerByAttribute_management(lyr,"REMOVE_FROM_SELECTION",""""SS_STATUS" = 'active'""")
    arcpy.AddMessage(lyr.definitionQuery)
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_ifw_sites_template.rlf",
                                  pdfPath,"USE_RLF")
    #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Marine Sample Site - All": #this will not remove any inactive sites from the selection
    layerName = "Marine Sample Site"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    arcpy.AddMessage(lyr.definitionQuery)
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_amw_sites_template.rlf",
                                  pdfPath,"USE_RLF")
    #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Freshwater Sample Site - All": #this will not remove any inactive sites from the selection
    layerName = "Freshwater Sample Site"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    arcpy.AddMessage(lyr.definitionQuery)
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_afw_sites_template.rlf",
                                  pdfPath,"USE_RLF")
    #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Pollution Source Inventory - Lines":
    layerName = "Pollution Source Inventory (Lines)"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_psi_lines_template.rlf",
                                  pdfPath,"USE_RLF")
    #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Pollution Source Inventory - Icons":
    layerName = "Pollution Source Inventory (Icons)"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_psi_icons_template.rlf",
                                  pdfPath,"USE_RLF")
    #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3        
elif reportType == "Pollution Source Inventory":
    layerName = "Pollution Source Inventory"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_psi_main_template.rlf",
                                  pdfPath,"USE_RLF")
   #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Pollution Source Inventory (Landscape)":
    layerName = "Pollution Source Inventory"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
    desc = arcpy.Describe(lyr)
    selectedFIDs = desc.FIDSet
    if len(selectedFIDs) > 0:
        arcpy.mapping.ExportReport(lyr,
                                  r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_psi_main_template_land.rlf",
                                  pdfPath,"USE_RLF")
   #Returns value so that proper status message can be sent
        successCheck = 1
    else:
        successCheck = 3
elif reportType == "Sample Site Classification - XLS file":
    reportSearchString = "SSC"
    lyrs = arcpy.mapping.ListLayers(mxd, "", df)
    for lyr in lyrs:
        if reportSearchString in lyr.name: 
            arcpy.SelectLayerByAttribute_management(lyr,"NEW_SELECTION",""""OBJECTID" > 0""")
	    arcpy.SelectLayerByAttribute_management(lyr,"REMOVE_FROM_SELECTION",""""SS_STATUS" = 'inactive'""")
	    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
            desc = arcpy.Describe(lyr)
            selectedFIDs = desc.FIDSet
            if len(selectedFIDs) > 0:
                arcpy.mapping.ExportReport(lyr,
                                            r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_ssc_sites_template.rlf",
                                            xlsPath,"USE_RLF")
                #Returns value so that proper status message can be sent
                successCheck = 4 #value 1 is "ok", 2 is SSC problem, 3 is fail, 4 is SSC XLS okay
                break
            else:
                successCheck = 3 #value 1 is "ok", 2 is SSC problem, 3 is fail
                break
        else:
           successCheck = 3
elif reportType == "Sample Site Classification - PDF file":
    reportSearchString = "SSC"
    lyrs = arcpy.mapping.ListLayers(mxd, "", df)
    for lyr in lyrs:
        if reportSearchString in lyr.name: 
            arcpy.SelectLayerByAttribute_management(lyr,"NEW_SELECTION",""""OBJECTID" > 0""")
	    arcpy.SelectLayerByAttribute_management(lyr,"REMOVE_FROM_SELECTION",""""SS_STATUS" = 'inactive'""")
	    #Code to check for selection in layer (borrowed from Babak's tools) and to escape the script if no selection exists
            desc = arcpy.Describe(lyr)
            selectedFIDs = desc.FIDSet
            if len(selectedFIDs) > 0:
                arcpy.mapping.ExportReport(lyr,
                                            r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_ssc_sites_template.rlf",
                                            pdfPath,"USE_RLF")
                #Returns value so that proper status message can be sent
                successCheck = 1 #value 1 is "ok", 2 is SSC problem, 3 is fail, 4 is SSC XLS okay
                break
            else:
                successCheck = 3 #value 1 is "ok", 2 is SSC problem, 3 is fail
                break
        else:
           successCheck = 3
elif reportType == "Vessel Waypoints":
    layerName = "Vessel Waypoints"
    lyr = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
    arcpy.mapping.ExportReport(lyr,
                               r"Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\SDMRS2_Tools\Report_Templates_Arc10\report_vway_template.rlf",
                               pdfPath,"USE_RLF")
   #Returns value so that proper status message can be sent
    successCheck = 1        
#Decides which end message to print       
if successCheck == 1:
    arcpy.AddWarning("###############################################")
    arcpy.AddWarning("###     Report created successfully!        ###")
    arcpy.AddWarning("###############################################")
    os.startfile(pdfPath)
elif successCheck == 2:
    arcpy.AddError("###########################################################")
    arcpy.AddError("###########################################################")
    arcpy.AddError("###            ERROR. No report created.                ###")
    arcpy.AddError("###   Cannot find the  \"SSC\" layer for SSC reports.   ###")
    arcpy.AddError("###########################################################")
    arcpy.AddError("###########################################################")  
elif successCheck == 3:
    arcpy.AddError("##########################################################################")
    arcpy.AddError("##########################################################################")
    arcpy.AddError("###                    ERROR. No report created.                       ###")
    arcpy.AddError("###   Please check for feature selections in your chosen layers.       ###")
    arcpy.AddError("##########################################################################")
    arcpy.AddError("##########################################################################")
elif successCheck == 4:
    arcpy.AddWarning("###############################################")
    arcpy.AddWarning("###     Report created successfully!        ###")
    arcpy.AddWarning("###############################################")
    os.startfile(xlsPath)
del mxd
