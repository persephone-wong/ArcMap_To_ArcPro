# Script Name: RemoveCharts.py
# Created by Sarah Bartnik
# Date: March 22, 2013
# Description: This script will remove charts loaded by previous scripts

# Import modules
import sys,os,math,string,arcpy
from arcpy import env

# Read from current map
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Data Themes")[0]
targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Charts", df)[0]

for lyr in targetGroupLayer:
        arcpy.mapping.RemoveLayer(df, lyr)
arcpy.RefreshActiveView() ## need to just map a new map with this. 
arcpy.RefreshTOC()