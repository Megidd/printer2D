import tkinter as tk
from tkinter import filedialog
import tempfile
import os

from barcode_scanner.process import compare

def main():
    root = tk.Tk()
    root.title("Barcode Comparator")

    def browse_input_csv_file():
        filename = filedialog.askopenfilename(title="Select Input CSV File", filetypes=[("CSV Files", "*.csv")])
        input_csv_file_entry.delete(0, tk.END)
        input_csv_file_entry.insert(0, filename)

    def run():
        input_barcode_txt = input_barcode_txt_text_box.get("1.0", tk.END)
        input_csv_file = input_csv_file_entry.get()

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_input_file:
            tmp_input_file.write(input_barcode_txt)
            input_barcode_txt_file = tmp_input_file.name

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_output_file:
            output_csv_file = tmp_output_file.name
            compare(input_barcode_txt_file, input_csv_file, output_csv_file)
            os.startfile(output_csv_file)

    input_barcode_txt_label = tk.Label(root, text="Input Barcode Text:")
    input_barcode_txt_label.grid(row=0, column=0, padx=5, pady=5)

    input_barcode_txt_text_box = tk.Text(root, height=10, width=50)
    input_barcode_txt_text_box.grid(row=0, column=1, padx=5, pady=5)

    input_csv_file_label = tk.Label(root, text="Input CSV File:")
    input_csv_file_label.grid(row=1, column=0, padx=5, pady=5)

    input_csv_file_entry = tk.Entry(root, width=50)
    input_csv_file_entry.grid(row=1, column=1, padx=5, pady=5)

    input_csv_file_browse_button = tk.Button(root, text="Browse", command=browse_input_csv_file)
    input_csv_file_browse_button.grid(row=1, column=2, padx=5, pady=5)

    run_button = tk.Button(root, text="RUN", command=run)
    run_button.grid(row=2, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as Ex:
        print(Ex)
