import os
import win32com.client as win32

objFSO = win32.Dispatch("Scripting.FileSystemObject")
ShellObj = win32.Dispatch("Shell.Application")
clawPDFQueue = win32.Dispatch("clawPDF.JobQueue")

fullPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Results\pagefile")

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

    printJob.SetProfileSetting("OutputFormat", "Txt")
    printJob.ConvertTo(fullPath+".txt")

    printJob.SetProfileSetting("OutputFormat", "Pdf")
    printJob.ConvertTo(fullPath+".pdf")

    if (not printJob.IsFinished or not printJob.IsSuccessful):
        print("Could not convert the file:", fullPath)
    else:
        print("Job finished successfully")

print("Releasing the object")
clawPDFQueue.ReleaseCom()
