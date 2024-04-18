import fitz  # Import the PyMuPDF library

def add_image_and_text_to_pdf(pdf_path, image_path, image_pos_x, image_pos_y, text, text_pos_x, text_pos_y,\
                              text1, text2, text3):
    # Open the existing PDF
    doc = fitz.open(pdf_path)

    # Select the first page of the PDF
    page = doc[0]

    # Add the image to the specified location
    page.insert_image(fitz.Rect(image_pos_x, image_pos_y, image_pos_x + 100, image_pos_y + 100), filename=image_path)

    # Add the text to the specified location
    # Note: The 'insert_text' method requires specifying the bottom-left corner of the text block
    page.insert_text((text_pos_x, text_pos_y), text, fontsize=11)

    page.insert_text((text_pos_x, text_pos_y+20), text1, fontsize=11)
    page.insert_text((text_pos_x, text_pos_y+40), text2, fontsize=11)
    page.insert_text((text_pos_x, text_pos_y+60), text3, fontsize=11)

    # Save the modified PDF
    doc.save(pdf_path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
