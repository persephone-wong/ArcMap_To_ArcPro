import arcpy, os, string
from arcpy import env
class ToolValidator(object):
  """Class for validating a tool's parameter values and controlling
  the behavior of the tool's dialog."""

  def __init__(self):
    """Setup arcpy and the list of tool parameters."""
    self.params = arcpy.GetParameterInfo()

  def initializeParameters(self):
    """Refine the properties of a tool's parameters.  This method is
    called when the tool is opened."""
    env.workspace = "Q:\GW\EC1210WQAEH_QESEA\CSSP_PYR\SDMRS2\Boundaries.gdb\BDY_MWQM_GA_Sectors_Poly"
    values = set()
    cur = arcpy.SearchCursor(env.workspace,'','', "SECTOR","SECTOR A")
    for row in cur:
        values.add(row.getValue("SECTOR"))
    targetList = sorted(values)
    self.params[0].filter.list = sorted(values)
    return

  def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""
    return

  def updateMessages(self):
    """Modify the messages created by internal validation for each tool
    parameter.  This method is called after internal validation."""
    return