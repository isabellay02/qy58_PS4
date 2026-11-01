# Import essential packages
import arcpy

inFC = arcpy.GetParameterAsText(0)

# Describe the dataset as a dictionary
desc = arcpy.da.Describe(inFC)

# Report the dataset path
arcpy.AddMessage(f"Dataset path: {desc['catalogPath']}")

# Report the extent to one decimal place
extent = desc["extent"]
arcpy.AddMessage(f"XMin: {extent.XMin:.1f}")
arcpy.AddMessage(f"YMin: {extent.YMin:.1f}")
arcpy.AddMessage(f"XMax: {extent.XMax:.1f}")
arcpy.AddMessage(f"YMax: {extent.YMax:.1f}")

# Report
if desc['datasetType'] == "FeatureClass":
    arcpy.AddWarning(f"Shape type: {desc['shapeType']}")
elif desc['datasetType'] == "RasterDataset":
    arcpy.AddWarning(f"Raster format: {desc['format']}")
    arcpy.AddWarning(f"Number of rows: {desc['height']}")
    arcpy.AddWarning(f"Number of columns: {desc['width']}")
else:
    arcpy.AddError(f"Dataset type: {desc['datasetType']}")