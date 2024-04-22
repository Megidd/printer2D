import os
import win32com.client as win32

from utils.process import analyze
from utils.tempfile import create_temp_file
from utils.overwrite import delete
from utils.send import send2printer

def main(csv_file_path):
    objFSO = win32.Dispatch("Scripting.FileSystemObject")
    ShellObj = win32.Dispatch("Shell.Application")
    clawPDFQueue = win32.Dispatch("clawPDF.JobQueue")

    print("Initializing clawPDF queue...")
    clawPDFQueue.Initialize()

    print("Please print to clawPDF ...")

    production_mode = False

    while True:
        print("Waiting for the job to arrive at the queue...")
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

        analyze(pdfPath, csv_file_path)

        send2printer(pdfPath)

        if production_mode:
            delete(pdfPath)

    print("Releasing the object")
    clawPDFQueue.ReleaseCom()

if __name__ == "__main__":
    csv_file_path = 'cutting-list.csv'
    try:
        main(csv_file_path)
    except Exception as Ex:
        print(Ex)

    # To prevent the window from closing immediately after run
    input("Finished. Press any key to continue . . .")
