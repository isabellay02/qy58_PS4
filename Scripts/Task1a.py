# Import essential packages
import arcpy

# Allow overwriting output
arcpy.env.overwriteOutput = True

# Create string variables
stream = "V:/qy58_PS4/Data/streams.shp"
distance = "1000 meters"
output = "V:/qy58_PS4/Scratch/StrmBuff1km.shp"

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