import fitz  # Import the PyMuPDF library

def create_pdf_with_image_and_text(pdfPath, qrPath, \
                                    project, floor, unit, \
                                    id_desc, \
                                    lengthXwidth, marginH, marginV, rowN, \
                                    ):
    # Create a new PDF document
    doc = fitz.open()

    # Define the page size in points (6 cm x 4 cm)
    page_width = 6 * 28.35  # Convert 6 cm to points
    page_height = 4 * 28.35  # Convert 4 cm to points

    # Add a new page to the document with specified dimensions
    page = doc.new_page(width=page_width, height=page_height)

    # Add the image to the specified location
    page.insert_image(fitz.Rect(50, 30, 50 + 50, 30 + 50), filename=qrPath)

    page.insert_font(fontname='my-font', fontfile= 'Tahoma.ttf', set_simple=False)

    # Add the text to the specified location
    page.insert_text((20, 92), id_desc, fontname='my-font', fontsize=12)

    page.insert_text((10+5, 20+5), project, fontname='my-font', fontsize=12)
    page.insert_text((10+5, 20+25), floor, fontname='my-font', fontsize=12)
    page.insert_text((10+5, 20+45), unit, fontname='my-font', fontsize=12)

    page.insert_text((40, 105), lengthXwidth, fontname='my-font', fontsize=12)
    page.insert_text((105, 80), rowN, fontname='my-font', fontsize=12)

    # margin == 0 : do nothing.
    if marginH == "1":
        page.insert_text((10, 5), "______", fontsize=36)
    elif marginH == "2":
        page.insert_text((10, 5), "______", fontsize=36)
        page.insert_text((10, 105), "______", fontsize=36)

    # margin == 0 : do nothing.
    if marginV == "1":
        page.insert_text((5, 38), "|", fontsize=36)
        page.insert_text((5, 68), "|", fontsize=36)
        page.insert_text((5, 100), "|", fontsize=36)
    elif marginV == "2":
        page.insert_text((5, 38), "|", fontsize=36)
        page.insert_text((5, 68), "|", fontsize=36)
        page.insert_text((5, 100), "|", fontsize=36)

        page.insert_text((130, 38), "|", fontsize=36)
        page.insert_text((130, 68), "|", fontsize=36)
        page.insert_text((130, 100), "|", fontsize=36)

    # Save the new PDF
    doc.save(pdfPath)
    doc.close()
