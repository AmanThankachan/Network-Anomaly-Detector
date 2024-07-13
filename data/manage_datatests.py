import pandas as pd
import os

# Directory containing the dataset CSV files has to be sourced from https://unsw-my.sharepoint.com/personal/z5025758_ad_unsw_edu_au/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset%2FCSV%20Files
dataset_dir = 'data/UNSW-NB15'

# List of CSV files to merge
csv_files = [
    'UNSW-NB15_1.csv',
    'UNSW-NB15_2.csv',
    'UNSW-NB15_3.csv',
    'UNSW-NB15_4.csv'
]

# Load and concatenate CSV files
dfs = [pd.read_csv(os.path.join(dataset_dir, csv_file)) for csv_file in csv_files]
merged_df = pd.concat(dfs, ignore_index=True)

# Save merged dataset to a new CSV file
merged_df.to_csv('data/network_traffic.csv', index=False)
