import os
import win32com.client as win32

objFSO = win32.Dispatch("Scripting.FileSystemObject")
ShellObj = win32.Dispatch("Shell.Application")
clawPDFQueue = win32.Dispatch("clawPDF.JobQueue")

fullPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Results\TestPage.pdf")

print("Initializing clawPDF queue...")
clawPDFQueue.Initialize()

print("Please print to clawPDF ...")

print("Waiting for the job to arrive at the queue...")

while True:
    print("Currently there are", clawPDFQueue.Count, "job(s) in the queue")
    printJob = clawPDFQueue.WaitForFirstJob()

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

    from utils.process import analyze
    analyze(fullPath)        

print("Releasing the object")
clawPDFQueue.ReleaseCom()

