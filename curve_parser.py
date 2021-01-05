import pandas as pd
import glob
import os

# making two methods to handle the parsing of power and thrust curves

# def parse_curve():
#     pass

# def format_curve():
#     pass

# def make_SAM_file():
#     """Method for compiling turbine data in the format for SAM."""
#     df = pd.DataFrame()

#     # Loop over turbine files
#     for tf in glob.glob("Reference.csv"):
#         pass
#         # Grab header first time through
#         # data = pd.read_csv(fpath + tf)
#         # Grab data 
#         # Append to dataframe

#     # Save dataframe as the SAM turbine input file

d = pd.read_csv("C:\\Users\\pduffy\\Documents\\Projects\\Turbines\\SAM_FORMAT_Wind Turbines.csv")
# print(d["Power Curve Array"].iloc[2])


data = pd.read_csv("C:\\Users\\pduffy\\Documents\\Projects\\Turbines\\wind-turbine-archive-dev\\dtu10_v1_data.csv")

d2 = data.astype(str)
print(d2, type(d2))
test_str = d2['Wind speed']

my_str = str()
for i in range(len(test_str)):
    if i == 0:
        my_str = my_str + test_str[i]
    else:
        my_str = my_str + ' | ' + test_str[i]

print(my_str)
