# Import essential package
import arcpy

# Input fields
inFC = arcpy.GetParameterAsText(0)
inField = arcpy.GetParameterAsText(1)

# Create variables
myPoint = arcpy.Point(X=597000, Y=249000)
rows = arcpy.da.SearchCursor(inFC, ["SHAPE@", inField])

# Search loop
for row in rows:
    recShape = row[0]
    print(row[1])
    if recShape.contains(myPoint):
        arcpy.AddMessage(f"{inField}: {row[1]}")
del rows