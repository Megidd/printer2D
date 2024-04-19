import csv
from utils.overwrite import move_and_overwrite
from utils.tempfile import create_temp_file

def find_and_delete_row(filename, varl_value=600, varw_value=700):
  id = ""
  name = ""
  project = ""
  floor = ""
  unit = ""

  tmpFile = create_temp_file("CUTTING-LIST-", ".csv")

  with open(filename, 'r', newline='') as csvfile, open(tmpFile, 'w', newline='') as new_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(new_file)

    found = False
    for row in reader:
      count = row[5]
      if count.isdigit():
        count = int(count)
      else:
        print("Warning: count string is not a valid integer.")
        continue
      if not found and count > 0 and row[7] == str(varl_value) and row[9] == str(varw_value) or \
        not found and count > 0 and row[7] == str(varw_value) and row[9] == str(varl_value):
        id, name = row[3], row[4]
        project, floor, unit = row[0], row[1], row[2]
        found = True
        row[5] = count -1
        print(f"Found line: {id}, {name}, count change: {count} > {row[5]}")
        writer.writerow(row)
      else:
        writer.writerow(row)

    if not found:
      print(f"Line with VARL: {varl_value} and VARW: {varw_value} is already handled on the CSV file.")

  move_and_overwrite(tmpFile, filename)
  return project, floor, unit, id, name
