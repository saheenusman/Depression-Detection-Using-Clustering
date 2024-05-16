import pandas as pd
import os

# Directory containing CSV files
directory = 'C:\\Users\\sahee\\Downloads\\mental health\\control'

# List to store DataFrame objects
dfs = []

# Iterate over each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Read CSV file into a DataFrame
        df = pd.read_csv(os.path.join(directory, filename))
        
        # Add a new column to indicate the source file
        df['Source'] = filename
        
        # Append DataFrame to the list
        dfs.append(df)

# Merge DataFrames row-wise
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged_data_control.csv', index=False)
