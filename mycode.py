import pandas as pd      # Used to work with table-like data
import os                # Used to create folders and file paths

# Create data in dictionary form (rows + columns)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],   # Names column
    'Age': [25, 30, 35],                   # Age column
    'City': ['New York', 'Los Angeles', 'Chicago']  # City column
}

# Convert dictionary data into a DataFrame (table)
df = pd.DataFrame(data)

# Adding new row to df for V2
new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# Adding new row to df for V3
# new_row_loc2 = {'Name': 'GF2', 'Age': 30, 'City': 'City2'}
# df.loc[len(df.index)] = new_row_loc2

# Name of the folder where the CSV file will be stored
data_dir = 'data'

# Create the folder if it does not already exist
os.makedirs(data_dir, exist_ok=True)

# Create the full path for the CSV file
# (folder name + file name)
file_path = os.path.join(data_dir, 'sample_data.csv')

# Store the DataFrame as a CSV file at the given file path
# index=False means "do not save row numbers"
df.to_csv(file_path, index=False)

# Print message to confirm where the file was saved
print(f"CSV file saved to {file_path}")