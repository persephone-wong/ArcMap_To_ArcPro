import arcpy
from arcpy import env

class ToolValidator(object):
    def __init__(self):
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        env.workspace = "Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\Boundaries.gdb\BDY_MWQM_GA_Sectors_Poly"
        Values = set()
        Cursor = arcpy.da.SearchCursor(env.workspace,'','', "SECTOR","SECTOR A")
        for row in Cursor:
            Values.add(row.getValue("SECTOR"))
        TargetList = sorted(Values)
        self.params[0].filter.list = sorted(Values)
        return
    
    def updateParameters(self):
        return
    
    def updateMessages(self):
        return