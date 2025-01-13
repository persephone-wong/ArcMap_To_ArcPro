import arcpy
from arcpy import env

class ToolValidator(object):
    def __init__(self):
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        env.workspace = 'Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\Boundaries.gdb'
        Values = set()
        try:
            with arcpy.da.SearchCursor("BDY_MWQM_GA_Sectors_Poly", ["SECTOR"]) as Cursor:
                for row in Cursor:
                    Values.add(row[0])  # Access the value directly from the tuple
                
            # Sort and set the filter list for the parameter
            TargetList = sorted(Values)
            self.params[0].filter.list = TargetList  # Set the list for the filter parameter
        except Exception as e:
            arcpy.AddError(f"Error while retrieving values from the feature class: {str(e)}")
        return
    
    def updateParameters(self):
        return
    
    def updateMessages(self):
        return