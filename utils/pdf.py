from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def add_image_and_text_to_pdf(pdf_path,
                              image_path, image_pos_x, image_pos_y,
                              text, text_pos_x, text_pos_y):
    """
    Adds an image and text to a single-page PDF.

    Args:
        pdf_path: Path to the PDF file.
        image_path: Path to the image file.
        image_pos_x: X-coordinate of the image position in mm.
        image_pos_y: Y-coordinate of the image position in mm.
        text: The text to add.
        text_pos_x: X-coordinate of the text position in mm.
        text_pos_y: Y-coordinate of the text position in mm.
    """
    c = canvas.Canvas(pdf_path)

    # Add image
    c.drawImage(image_path, image_pos_x * mm, image_pos_y * mm)

    # Add text
    c.setFont("Helvetica", 12)
    c.drawString(text_pos_x * mm, text_pos_y * mm, text)

    c.save()
