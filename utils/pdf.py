import fitz  # Import the PyMuPDF library

def create_pdf_with_image_and_text(output_pdf_path, image_path, image_pos_x, image_pos_y, text, text_pos_x, text_pos_y, text_extra1, text_extra2, text_extra3, text_extra_x, text_extra_y):
    # Create a new PDF document
    doc = fitz.open()

    # Define the page size in points (6 cm x 4 cm)
    page_width = 6 * 28.35  # Convert 6 cm to points
    page_height = 4 * 28.35  # Convert 4 cm to points

    # Add a new page to the document with specified dimensions
    page = doc.new_page(width=page_width, height=page_height)

    # Add the image to the specified location
    page.insert_image(fitz.Rect(image_pos_x, image_pos_y, image_pos_x + 42, image_pos_y + 42), filename=image_path)

    # Add the text to the specified location
    page.insert_text((text_pos_x, text_pos_y), text, fontsize=10)

    page.insert_text((text_extra_x, text_extra_y), text_extra1, fontsize=10)
    page.insert_text((text_extra_x+80, text_extra_y), text_extra2, fontsize=10)
    page.insert_text((text_extra_x+110, text_extra_y), text_extra3, fontsize=10)

    # Save the new PDF
    doc.save(output_pdf_path)
    doc.close()
