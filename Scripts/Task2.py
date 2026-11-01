# Import essential packages
import arcpy
from pathlib import Path

# Set paths
script_path = Path(__file__).resolve().parent
data_path = script_path.parent / 'Data'
scratch_path = script_path.parent / 'Scratch'

# Arcpy environment settings
arcpy.env.overwriteOutput = True # Allow arcpy to overwrite output

# Create variables
roads = str(data_path / 'Roads.shp')
multi_value_input = "0;201;203"
road_types = multi_value_input.split(";")

# Select tool loop
for road_type in road_types:
    arcpy.analysis.Select(
        roads, 
        str(scratch_path / f"roads_{road_type}.shp"), 
        f"ROAD_TYPE = {road_type}"
        )

# Display geoprocessing messages
print(arcpy.GetMessages())