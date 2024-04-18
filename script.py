import os
import win32com.client as win32

objFSO = win32.Dispatch("Scripting.FileSystemObject")
ShellObj = win32.Dispatch("Shell.Application")
clawPDFQueue = win32.Dispatch("clawPDF.JobQueue")

from utils.process import analyze
from utils.tempfile import create_temp_file

print("Initializing clawPDF queue...")
clawPDFQueue.Initialize()

print("Please print to clawPDF ...")

print("Waiting for the job to arrive at the queue...")

while True:
    print("Currently there are", clawPDFQueue.Count, "job(s) in the queue")
    printJob = clawPDFQueue.WaitForFirstJob()

    printJob.SetProfileByGuid("DefaultGuid")
    
    pdfPath = create_temp_file(prefix="WinCAM-label-", suffix=".pdf")
    print(f"Temp file created at: {pdfPath}")

    out_dir = os.path.dirname(pdfPath)
    if not os.path.exists(out_dir):
        print("Creating output directory:", out_dir)
        os.makedirs(out_dir)

    printJob.SetProfileSetting("OutputFormat", "Pdf")
    printJob.SetProfileSetting("OpenViewer", False)
    printJob.ConvertTo(pdfPath)

    if (not printJob.IsFinished or not printJob.IsSuccessful):
        print("Could not convert the file:", pdfPath)
    else:
        print("Job finished successfully")

    analyze(pdfPath)        

print("Releasing the object")
clawPDFQueue.ReleaseCom()

