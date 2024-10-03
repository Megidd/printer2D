import os
from KD.process import openCSV
from utils.tempfile import create_temp_file

def main(csvPath):
    csvPath_splitByComma = create_temp_file(prefix="split-by-comma-", suffix=".csv")
    print(f"Temp file created at: {csvPath_splitByComma}")

    out_dir = os.path.dirname(csvPath_splitByComma)
    if not os.path.exists(out_dir):
        print("Creating output directory:", out_dir)
        os.makedirs(out_dir)

    openCSV(csvPath, csvPath_splitByComma)

if __name__ == "__main__":
    csv_file_path = 'test.csv'
    try:
        main(csv_file_path)
    except Exception as Ex:
        print(Ex)

    # To prevent the window from closing immediately after run
    input("Finished. Press any key to continue . . .")
