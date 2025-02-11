import os
from barcode_scanner.process import compare
from utils.tempfile import create_temp_file

def main(txtPath, csvPath):
    print("Input barcode text file: ", txtPath)
    print("Input CSV file: ", csvPath)

    csvPath_barcode_scanner = create_temp_file(prefix="barcode_scanner--", suffix=".csv")
    print(f"Temp file created at: {csvPath_barcode_scanner}")

    out_dir = os.path.dirname(csvPath_barcode_scanner)
    if not os.path.exists(out_dir):
        print("Creating output directory:", out_dir)
        os.makedirs(out_dir)

    compare(txtPath, csvPath, csvPath_barcode_scanner)

if __name__ == "__main__":
    txt_file_path = 'barcode-scanner.txt'
    csv_file_path = 'CUTTING-LIST (1).csv'
    try:
        main(txt_file_path, csv_file_path)
    except Exception as Ex:
        print(Ex)

    # To prevent the window from closing immediately after run
    input("Finished. Press any key to continue . . .")
