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
    # Create a TextWriter object for the page
    writer = fitz.TextWriter(page.rect)

    # Use the TextWriter to add Hebrew text
    writer.append((20, 92), id_desc, fontsize=11, right_to_left=True, language='ar')
    writer.append((10+5, 20+5), project, fontsize=12, right_to_left=False, language='ar')
    writer.append((10+5, 20+25), floor, fontsize=12, right_to_left=False, language='ar')
    writer.append((10+5, 20+45), unit, fontsize=12, right_to_left=False, language='ar')
    writer.append((40, 105), lengthXwidth, fontsize=12, right_to_left=False, language='ar')
    writer.append((105, 80), rowN, fontsize=12, right_to_left=False, language='ar')

    writer.write_text(page)

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
