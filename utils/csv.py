import csv

def find_and_delete_row(filename, varl_value=600, varw_value=700):
  first_value = ""
  second_value = ""

  with open(filename, 'r', newline='') as csvfile, open(filename + '_modified.csv', 'w', newline='') as new_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(new_file)

    found = False
    for row in reader:
      if not found and row[6] == str(varl_value) and row[8] == str(varw_value) or \
        not found and row[6] == str(varw_value) and row[8] == str(varl_value):
        first_value, second_value = row[3], row[4]
        found = True
        print(f"Found line: {first_value}, {second_value}")
      else:
        writer.writerow(row)

    if not found:
      print(f"Line with VARL: {varl_value} and VARW: {varw_value} not found.")

  return first_value, second_value

  # Delete the original file (optional)
  # import os
  # os.remove(filename)
