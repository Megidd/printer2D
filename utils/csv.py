import csv

def find_and_delete_row(filename, varl_value=600, varw_value=700):
  """
  Finds the line with specific values after VARL and VARW, extracts the 1st and 2nd values,
  and deletes that line from the CSV file.

  Args:
      filename: The path to the CSV file.
      varl_value: The desired value after the VARL column (default: 600).
      varw_value: The desired value after the VARW column (default: 700).
  """

  with open(filename, 'r', newline='') as csvfile, open(filename + '_modified.csv', 'w', newline='') as new_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(new_file)

    found = False
    for row in reader:
      if not found and row[3] == str(varl_value) and row[5] == str(varw_value) or \
        not found and row[3] == str(varw_value) and row[5] == str(varl_value):
        first_value, second_value = row[0], row[1]
        found = True
        print(f"Found line: {first_value}, {second_value}")
      else:
        writer.writerow(row)

    if not found:
      print(f"Line with VARL: {varl_value} and VARW: {varw_value} not found.")

  # Delete the original file (optional)
  # import os
  # os.remove(filename)