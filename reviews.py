# a#Practice winmag_data
import pandas as pd

import zipfile

# Path to the ZIP file
zip_file_path = 'data/winemag-data-130k-v2.csv.zip'
csv_file_name = 'winemag-data-130k-v2.csv'
output_file_path = 'data/reviews-per-country.csv'

# Extract the CSV file from the ZIP archive
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extract(csv_file_name, 'data')

# Read the CSV file into a DataFrame
df = pd.read_csv(f'data/{csv_file_name}')

# Create a summary of the data by country
summary = df.groupby('country').agg(
    count=('country', 'size'),
    points=('points', 'mean')
).reset_index()

# Round the points column to 1 decimal point
summary['points'] = summary['points'].round(1)

# Save the summary to a new CSV file
summary.to_csv(output_file_path, index=False)

print(f"Summary data has been written to {output_file_path}")

print(summary)