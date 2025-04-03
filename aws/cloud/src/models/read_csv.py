import pandas as pd

# Define the path to the CSV file
csv_file_path = '../../exports/'
csv_name_df = 'nu4930001-sofy-bancoagricola-pdn-sessions.csv'
path_to_csv = csv_file_path + csv_name_df

# Read the CSV file into a DataFrame
df = pd.read_csv(path_to_csv, sep=',', header=0)

# Print the number of rows in the DataFrame
print(f"Number of rows in the DataFrame: {df.shape[0]}")