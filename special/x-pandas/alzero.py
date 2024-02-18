# ========================================
# Data Science
# Convert Text To CSV And Control Columns
# ========================================

# Import Pandas Tool
# pip install pandas
import pandas

# Get All Methods Of Pandas
print(dir(pandas))

# Convert & Disable Indexing
my_data = pandas.read_csv("points.txt")
print(my_data)
my_data.to_csv("points.csv", index=None)

# Add Your Own Columns
my_data = pandas.read_csv("points.txt")
my_data.columns = ["Name", "Points"]
my_data.to_csv("points.csv", index=None)

# Specify Delimiter
my_data = pandas.read_csv("points.txt", delimiter="=")
my_data.columns = ["Name", "Points"]
my_data.to_csv("points.csv", index=None)
