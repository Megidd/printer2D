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

numbers = [int(re.search(r'\d+', item).group()) for item in matches]

# Filter the numbers greater than 5
filtered_numbers = [num for num in numbers if num > 5]

print(filtered_numbers)

if len(filtered_numbers) < 2:
  print("Not expected: the list has less than two items.")

from utils.csv import find_and_delete_row

id, name = find_and_delete_row("CUTTING-LIST.csv", filtered_numbers[0], filtered_numbers[1])
print(f"Found: ID: {id}, name: {name}")

identity = f"{id}-{name}"

import segno

qrcode = segno.make_qr(identity)

qrPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Results\qrcode.png")

qrcode.save(
    qrPath,
    scale=5,
    border=2,
)

from utils.pdf import add_image_and_text_to_pdf

add_image_and_text_to_pdf(fullPath, qrPath, 200, 100, identity, 200, 50)
