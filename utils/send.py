import os
import shutil
import subprocess

def send2printer(pdfPath):
    # https://mendelson.org/pdftoprinter.html
    # https://stackoverflow.com/a/47994723/3405291
    toPrinterPath = shutil.which("PDFtoPrinter.exe")
    if toPrinterPath is not None:
        subprocess.run(f'PDFtoPrinter.exe "{pdfPath}"', shell=True)
    else:
        print(f'Missing "PDFtoPrinter.exe":')
        print("https://github.com/emendelson/pdftoprinter/blob/main/PDFtoPrinter.exe?raw=true")
        os.startfile(pdfPath, "print")
