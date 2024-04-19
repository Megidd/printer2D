import fitz # pip install PyMuPDF # https://stackoverflow.com/a/63518022/3405291
import os
import re
import segno
from utils.csv import find_and_delete_row
from utils.pdf import add_image_and_text_to_pdf
from utils.tempfile import create_temp_file

def analyze(pdfPath, csv_file_path):

    with fitz.open(pdfPath) as doc:
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
        return

    project, floor, unit, id, name = find_and_delete_row(csv_file_path, filtered_numbers[0], filtered_numbers[1])
    print(f"Found: ID: {id}, name: {name}")

    identity = f"{id}-{name}"

    qrcode = segno.make_qr(identity)

    qrPath = create_temp_file("QR-", ".png")
    print(f"Temp file created at: {qrPath}")

    qrcode.save(
        qrPath,
        scale=4,
        border=0,
    )

    add_image_and_text_to_pdf(pdfPath, qrPath, 10, 68, identity, 55, 92,\
                            f"P: {project}", f"F: {floor}", f"U: {unit}", 5, 20)
