import csv
import codecs

def compare(input_barcode_txt_file, input_csv_file, output_csv_file):
    # Create a map from the text file
    qr_map = {}
    with open(input_barcode_txt_file, 'r') as f:
        for line in f:
            qr_code = line.strip()
            if qr_code in qr_map:
                qr_map[qr_code] += 1
            else:
                qr_map[qr_code] = 1

    # Read the CSV file and modify it
    with codecs.open(input_csv_file, 'r', encoding='cp1256') as f:
        reader = csv.reader(f, delimiter=',')
        rows = [row for row in reader]

    # Modify the rows based on the qr_map
    modified_rows = []
    for row in rows:
        combined_key = (row[9] + '-' + row[10]).strip()
        if combined_key in qr_map:
            row[4] = int(row[4]) - qr_map[combined_key]
        modified_rows.append(row)

    # Delete the zero counts
    # It means only keep a row if the count is _not_ zero
    modified_rows_filtered = []
    for row in modified_rows:
        if row[4] != 0:
            modified_rows_filtered.append(row)

    # Save the modified CSV file
    with codecs.open(output_csv_file, 'w', encoding='cp1256') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(modified_rows_filtered)
