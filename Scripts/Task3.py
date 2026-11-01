# Import essential packages
import arcpy
from pathlib import Path

# Set paths
script_path = Path(__file__).resolve().parent
data_path = script_path.parent / 'Data'
scratch_path = script_path.parent / 'Scratch'

# Arcpy environment settings
arcpy.env.overwriteOutput = True # Allow arcpy to overwrite output
arcpy.env.workspace = str(data_path) # Set the folder to search

# List feature classes with names start with BMR
bmr_features = arcpy.ListFeatureClasses("BMR*")
county = str(data_path / "TriCounties.shp")

for bmr_feature in bmr_features:
    # Set output workspace
    out_workspace = str(scratch_path / bmr_feature[:-4])
    # Create folders
    arcpy.management.CreateFolder(
        scratch_path, 
        bmr_feature[:-4]
        )
    arcpy.analysis.Split(
        in_features = bmr_feature, 
        split_features = county, 
        split_field = "CO_NAME", 
        out_workspace=out_workspace
        )
    # Display geoprocessing messages
    print(arcpy.GetMessages())