import fitz # pip install PyMuPDF # https://stackoverflow.com/a/63518022/3405291
import os
import re
import segno
from utils.csv import find_and_delete_row
from utils.pdf import create_pdf_with_image_and_text
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

    project, floor, unit, id, desc, name, length, marginH, width, marginV, rowN = \
        find_and_delete_row(csv_file_path, filtered_numbers[0], filtered_numbers[1])
    print(f"Found: ID: {id}, description: {desc}, name: {name}")

    id_name = f"{id}-{name}"

    qrcode = segno.make_qr(id_name)

    qrPath = create_temp_file("QR-", ".png")
    print(f"Temp file created at: {qrPath}")

    qrcode.save(
        qrPath,
        scale=4,
        border=0,
    )

    id_desc = f"{id}-{desc}"

    create_pdf_with_image_and_text(pdfPath, qrPath, \
                                   f"P: {project}", f"F: {floor}", f"U: {unit}", \
                                    id_desc, \
                                        f"LxW: {length} x {width}", f" __ : {marginH}", f" | : {marginV}", f"r: {rowN}", \
                                   )
