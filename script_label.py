import tkinter as tk
from tkinter import filedialog

from barcode_scanner.process import compare

def main():
    root = tk.Tk()
    root.title("Barcode Comparator")

    def browse_input_barcode_txt_file():
        filename = filedialog.askopenfilename(title="Select Input Barcode Text File", filetypes=[("Text Files", "*.txt")])
        input_barcode_txt_file_entry.delete(0, tk.END)
        input_barcode_txt_file_entry.insert(0, filename)

    def browse_input_csv_file():
        filename = filedialog.askopenfilename(title="Select Input CSV File", filetypes=[("CSV Files", "*.csv")])
        input_csv_file_entry.delete(0, tk.END)
        input_csv_file_entry.insert(0, filename)

    def browse_output_csv_file():
        filename = filedialog.asksaveasfilename(title="Select Output CSV File", defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        output_csv_file_entry.delete(0, tk.END)
        output_csv_file_entry.insert(0, filename)

    def run():
        input_barcode_txt_file = input_barcode_txt_file_entry.get()
        input_csv_file = input_csv_file_entry.get()
        output_csv_file = output_csv_file_entry.get()
        compare(input_barcode_txt_file, input_csv_file, output_csv_file)

    root = tk.Tk()
    root.title("Barcode Comparator")

    input_barcode_txt_file_label = tk.Label(root, text="Input Barcode Text File:")
    input_barcode_txt_file_label.grid(row=0, column=0, padx=5, pady=5)

    input_barcode_txt_file_entry = tk.Entry(root, width=50)
    input_barcode_txt_file_entry.grid(row=0, column=1, padx=5, pady=5)

    input_barcode_txt_file_browse_button = tk.Button(root, text="Browse", command=browse_input_barcode_txt_file)
    input_barcode_txt_file_browse_button.grid(row=0, column=2, padx=5, pady=5)

    input_csv_file_label = tk.Label(root, text="Input CSV File:")
    input_csv_file_label.grid(row=1, column=0, padx=5, pady=5)

    input_csv_file_entry = tk.Entry(root, width=50)
    input_csv_file_entry.grid(row=1, column=1, padx=5, pady=5)

    input_csv_file_browse_button = tk.Button(root, text="Browse", command=browse_input_csv_file)
    input_csv_file_browse_button.grid(row=1, column=2, padx=5, pady=5)

    output_csv_file_label = tk.Label(root, text="Output CSV File:")
    output_csv_file_label.grid(row=2, column=0, padx=5, pady=5)

    output_csv_file_entry = tk.Entry(root, width=50)
    output_csv_file_entry.grid(row=2, column=1, padx=5, pady=5)

    output_csv_file_browse_button = tk.Button(root, text="Browse", command=browse_output_csv_file)
    output_csv_file_browse_button.grid(row=2, column=2, padx=5, pady=5)

    run_button = tk.Button(root, text="RUN", command=run)
    run_button.grid(row=3, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as Ex:
        print(Ex)
