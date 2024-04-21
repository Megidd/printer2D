import fitz  # Import the PyMuPDF library

def create_pdf_with_image_and_text(pdfPath, qrPath, \
                                    project, floor, unit, \
                                    id_desc, \
                                    length, marginH, width, marginV, rowN, \
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

    # Add the text to the specified location
    page.insert_text((20, 92), id_desc, fontsize=12)

    page.insert_text((10+5, 20+5), project, fontsize=12)
    page.insert_text((10+5, 20+25), floor, fontsize=12)
    page.insert_text((10+5, 20+45), unit, fontsize=12)

    page.insert_text((10, 10), length, fontsize=12)
    page.insert_text((10, 10), marginH, fontsize=12)
    page.insert_text((10, 10), width, fontsize=12)
    page.insert_text((10, 10), marginV, fontsize=12)
    page.insert_text((10, 20), rowN, fontsize=12)

    # Save the new PDF
    doc.save(pdfPath)
    doc.close()
