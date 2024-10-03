import csv
import pandas as pd

def openCSV(input_file):
    print("input file is ", input_file)

    # Load the CSV file
    output_file = "{input_file}--comma-separated.csv".format(input_file=input_file)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file, encoding='cp1256')

    # Split the 'Description' column into multiple columns based on comma
    split_descriptions = df['Description'].str.split(',', expand=True)

    # Rename the columns to Description0, Description1, Description2, etc.
    split_descriptions.columns = [f'Description{i}' for i in range(split_descriptions.shape[1])]

    # Combine the original data with the newly created columns
    df_updated = pd.concat([df.drop(columns=['Description']), split_descriptions], axis=1)

    # Save the updated DataFrame into a new CSV file
    df_updated.to_csv(output_file, index=False)

    print(f"Updated CSV file saved as {output_file}")
