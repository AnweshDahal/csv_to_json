# Required imports, will be replaced by bundled packages in next version
import pandas as pd # pandas for reading and working with the csv file 
import json # json for converting python data structure to json

# Get the file name
file_name = input('Enter the file name (without extension): ')

# The files to be converted must be kept inside the data folder
# In the next version, a simple flask web view will be bundled
# for a dynamic file load
df = pd.read_csv(f'./data/{file_name}.csv')

# Column name of the CSV
df_head = []

for row in df.columns:
  df_head.append(row)

data = list() # This will store the list of dictionaries

for index, row in df.iterrows():
  temp = dict() # This will store the data of each row of the CSV
  for column_name in df_head:
    temp.update({ f'{column_name}': f'{row[column_name]}'})
  data.append(temp) # append dictionary to the list


# Create a json object from the list of dictionaries
json_file = json.dumps(data, indent=2)

# Create a json file
with open(f'./data/json/{file_name}.json', "w") as outfile:
  outfile.write(json_file)

# Close the file writer
outfile.close()



# print(df_head)

# temp = {}
# for row in df.index:
#   _temp = {}
#   for col in df_head:
#     _temp.update({ col: df[]})
    
  