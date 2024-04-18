import os
import re

def analyze(pdfPath):
    import fitz # pip install PyMuPDF # https://stackoverflow.com/a/63518022/3405291

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

    from utils.csv import find_and_delete_row

    project, floor, unit, id, name = find_and_delete_row("CUTTING-LIST.csv", filtered_numbers[0], filtered_numbers[1])
    print(f"Found: ID: {id}, name: {name}")

    identity = f"{id}-{name}"

    import segno

    qrcode = segno.make_qr(identity)

    qrPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\Results\qrcode.png")

    qrcode.save(
        qrPath,
        scale=5,
        border=2,
    )

    from utils.pdf import add_image_and_text_to_pdf

    add_image_and_text_to_pdf(pdfPath, qrPath, 200, 120, identity, 200, 50,\
                            f"Project: {project}", f"Floor: {floor}", f"Unit: {unit}")