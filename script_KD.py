from KD.process import openCSV


def main(csv_file_path):
    openCSV(csv_file_path)

if __name__ == "__main__":
    csv_file_path = 'test.csv'
    try:
        main(csv_file_path)
    except Exception as Ex:
        print(Ex)

    # To prevent the window from closing immediately after run
    input("Finished. Press any key to continue . . .")
