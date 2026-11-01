# Import essential packages
import arcpy
from pathlib import Path

# Set paths
script_path = Path(__file__).resolve().parent
data_path = script_path.parent / 'Data'
scratch_path = script_path.parent / 'Scratch'

# Arcpy environment settings
arcpy.env.overwriteOutput = True # Allow arcpy to overwrite output
arcpy.env.workspace = str(data_path) # Set the default workspaces

# Create string variables
stream = "streams.shp"
distance = "1000 meters"
output = str(scratch_path / "StrmBuffer1km.shp")

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