import os
import shutil
import subprocess

def send2printer(pdfPath):
    AcrobatReaderPath = shutil.which("AcroRd32.exe")
    if AcrobatReaderPath is not None:
        subprocess.run(f'AcroRd32.exe /t "{pdfPath}"', shell=True)
    else:
        os.startfile(pdfPath, "print")
