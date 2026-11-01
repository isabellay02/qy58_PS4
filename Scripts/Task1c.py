# Import essential packages
import arcpy
import sys
from pathlib import Path
print(sys.argv)

# Set paths
script_path = Path(__file__).resolve().parent
data_path = script_path.parent / 'Data'
scratch_path = script_path.parent / 'Scratch'

# Arcpy environment settings
arcpy.env.overwriteOutput = True # Allow arcpy to overwrite output
arcpy.env.workspace = str(data_path) # Set the default workspaces

# Create string variables
stream = "streams.shp"
distance_input = sys.argv[1]
distance = f"{distance_input} meters"
output = sys.argv[2]

# Buffer streams and dissolve into one feature
arcpy.analysis.Buffer(
    stream,
    output,
    distance,
    "FULL",
    "ROUND",
    "ALL",
    "",
    "PLANAR"
)

# Display geoprocessing messages
print(arcpy.GetMessages())