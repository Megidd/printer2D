import os
import re
import win32com.client as win32

objFSO = win32.Dispatch("Scripting.FileSystemObject")
ShellObj = win32.Dispatch("Shell.Application")
clawPDFQueue = win32.Dispatch("clawPDF.JobQueue")

fullPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Results\TestPage.pdf")

print("Initializing clawPDF queue...")
clawPDFQueue.Initialize()

print("Please print to clawPDF ...")

print("Waiting for the job to arrive at the queue...")
if not clawPDFQueue.WaitForJob(60):
    print("The print job did not reach the queue within 60 seconds")
else:
    print("Currently there are", clawPDFQueue.Count, "job(s) in the queue")
    print("Getting job instance")
    printJob = clawPDFQueue.NextJob

    printJob.SetProfileByGuid("DefaultGuid")

    out_dir = os.path.dirname(fullPath)
    if not os.path.exists(out_dir):
        print("Creating output directory:", out_dir)
        os.makedirs(out_dir)

    printJob.SetProfileSetting("OutputFormat", "Pdf")
    printJob.SetProfileSetting("OpenViewer", False)
    printJob.ConvertTo(fullPath)

    if (not printJob.IsFinished or not printJob.IsSuccessful):
        print("Could not convert the file:", fullPath)
    else:
        print("Job finished successfully")

print("Releasing the object")
clawPDFQueue.ReleaseCom()

import fitz # pip install PyMuPDF # https://stackoverflow.com/a/63518022/3405291

with fitz.open(fullPath) as doc:
    text = ""
    for page in doc:
        text += page.get_text()

print(text)

matches = re.findall(r"\b(\d+mm)\b", text)
print(matches)
