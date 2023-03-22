import pandas as pd

# Load the CSV files into dataframes
supported_pairs_df = pd.read_csv('Test_files/Abhishek_output.csv')
output_df = pd.read_csv('output.csv')

# Merge the two dataframes based on source language and target language
merged_df = pd.merge(supported_pairs_df, output_df, on=['source language', 'target language'])

# Calculate the accuracy by comparing the translation engine column with the preferred engine column
accuracy_df = merged_df[merged_df['translation engine'] == merged_df['engine name']]
accuracy = len(accuracy_df) / len(output_df) * 100
print(f"Accuracy: {accuracy:.2f}%")
