import csv

def find_and_delete_row(filename, varl_value=600, varw_value=700):
  id = ""
  name = ""
  project = ""
  floor = ""
  unit = ""

  with open(filename, 'r', newline='') as csvfile, open(filename + '_modified.csv', 'w', newline='') as new_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(new_file)

    found = False
    for row in reader:
      if not found and row[6] == str(varl_value) and row[8] == str(varw_value) or \
        not found and row[6] == str(varw_value) and row[8] == str(varl_value):
        id, name = row[3], row[4]
        project, floor, unit = row[0], row[1], row[2]
        found = True
        print(f"Found line: {id}, {name}")
      else:
        writer.writerow(row)

    if not found:
      print(f"Line with VARL: {varl_value} and VARW: {varw_value} not found.")

  return project, floor, unit, id, name

  # Delete the original file (optional)
  # import os
  # os.remove(filename)
