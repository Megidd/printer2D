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
  marginVSide = ""
  pre = ""
  note = ""
  
  tmpFile = create_temp_file("cutting-list-", ".csv")

  with open(filename, 'r', encoding='cp1256', newline='', errors='replace') as csvfile, open(tmpFile, 'w', newline='', encoding='cp1256') as new_file:
    reader = csv.reader(csvfile)
    writer = csv.writer(new_file)

    rowInt = 0

    found = False
    for row in reader:
      rowInt = rowInt+1
      count = row[4]
      if count.isdigit():
        count = int(count)
      else:
        print("Warning: count string is not a valid integer.")
        continue
      if not found and count > 0 and row[0] == str(varl_value) and row[2] == str(varw_value) or \
        not found and count > 0 and row[0] == str(varw_value) and row[2] == str(varl_value):
        project, floor, unit = row[11], row[12], row[13]
        id, desc, name = row[9], row[8], row[10] # ID, Tag, Qrcode
        length, marginH, width, marginV = row[0], row[1], row[2], row[3]
        marginVSide = row[15]
        pre = row[16]
        note = row[17]
        rowN = f"{rowInt}"
        found = True
        row[4] = count -1
        print(f"Found line: {id}, {name}, count change: {count} > {row[4]}")
        writer.writerow(row)
      else:
        writer.writerow(row)

    if not found:
      print(f"Line with VARL: {varl_value} and VARW: {varw_value} is already handled on the CSV file.")

  move_and_overwrite(tmpFile, filename)
  return project, floor, unit, id, desc, name, length, marginH, width, marginV, rowN, marginVSide, pre, note
