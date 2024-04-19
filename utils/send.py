import os
import shutil
import subprocess

def send2printer(pdfPath):
    # https://mendelson.org/pdftoprinter.html
    toPrinterPath = shutil.which("PDFtoPrinter.exe")
    if toPrinterPath is not None:
        subprocess.run(f'PDFtoPrinter.exe "{pdfPath}"', shell=True)
    else:
        os.startfile(pdfPath, "print")
