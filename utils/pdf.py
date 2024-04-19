import fitz  # Import the PyMuPDF library

def add_image_and_text_to_pdf(pdf_path, image_path, image_pos_x, image_pos_y, text, text_pos_x, text_pos_y,\
                              text_extra1, text_extra2, text_extra3, text_extra_x, text_extra_y):
    # Open the existing PDF
    doc = fitz.open(pdf_path)

    # Select the first page of the PDF
    page = doc[0]

    # Add the image to the specified location
    page.insert_image(fitz.Rect(image_pos_x, image_pos_y, image_pos_x + 45, image_pos_y + 45), filename=image_path)

    # Before adding text, draw a white rectangle as the background
    # Adjust the rectangle size and position as needed to cover the text area
    text_bg_rect = fitz.Rect(text_pos_x, text_pos_y - 10, text_pos_x + 200, text_pos_y + 10)  # Example rectangle; adjust size as needed
    page.draw_rect(text_bg_rect, color=(1, 1, 1), fill=(1, 1, 1))  # Draw white rectangle

    # Add the text to the specified location
    # Note: The 'insert_text' method requires specifying the bottom-left corner of the text block
    page.insert_text((text_pos_x, text_pos_y), text, fontsize=10)

    # For extra text, repeat the process of drawing a white background then adding text
    # Adjust the rectangle size and position as needed for each text block
    text_extra_bg_rect = fitz.Rect(text_extra_x, text_extra_y - 10, text_extra_x + 350, text_extra_y + 10)  # Adjust size as needed
    page.draw_rect(text_extra_bg_rect, color=(1, 1, 1), fill=(1, 1, 1))  # Draw white rectangle for extra text

    page.insert_text((text_extra_x, text_extra_y), text_extra1, fontsize=10)
    page.insert_text((text_extra_x+80, text_extra_y), text_extra2, fontsize=10)
    page.insert_text((text_extra_x+110, text_extra_y), text_extra3, fontsize=10)

    # Save the modified PDF
    doc.save(pdf_path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
