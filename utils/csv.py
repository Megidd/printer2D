import csv
from utils.overwrite import move_and_overwrite
from utils.tempfile import create_temp_file

def find_and_delete_row(filename, varl_value=600, varw_value=700):
  project = ""
  floor = ""
  unit = ""
  id = ""
  desc = ""
  name = ""
  length = ""
  marginH = ""
  width = ""
  marginV = ""
  rowN = ""
  
  tmpFile = create_temp_file("CUTTING-LIST-", ".csv")

  with open(filename, 'r', newline='', errors='ignore') as csvfile, open(tmpFile, 'w', newline='') as new_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(new_file)

    rowInt = 0

    found = False
    for row in reader:
      rowInt = rowInt+1
      count = row[6]
      if count.isdigit():
        count = int(count)
      else:
        print("Warning: count string is not a valid integer.")
        continue
      if not found and count > 0 and row[8] == str(varl_value) and row[11] == str(varw_value) or \
        not found and count > 0 and row[8] == str(varw_value) and row[11] == str(varl_value):
        project, floor, unit = row[0], row[1], row[2]
        id, desc, name = row[3], row[4], row[5]
        length, marginH, width, marginV = row[8], row[9], row[11], row[12]
        rowN = f"{rowInt}"
        found = True
        row[5] = count -1
        print(f"Found line: {id}, {name}, count change: {count} > {row[5]}")
        writer.writerow(row)
      else:
        writer.writerow(row)

    if not found:
      print(f"Line with VARL: {varl_value} and VARW: {varw_value} is already handled on the CSV file.")

  move_and_overwrite(tmpFile, filename)
  return project, floor, unit, id, desc, name, length, marginH, width, marginV, rowN
