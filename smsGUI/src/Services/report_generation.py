import PyPDF2
import getpass
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def create_pdf_with_image(image_path1, image_path2, image_path3):
    """

    :param image_path1: result of image comparison
    :param image_path2: current DUT (device under test)
    :param image_path3: perfect sample of the current DUT
    :return: NoneType

    """
    current_time = datetime.now()
    current_time_name = current_time.strftime('%Y-%m-%d_%H_%M_%S')

    current_user = getpass.getuser()

    # Assume report directory structure is consistent
    output_filename = f'Reports\\Report_{current_time_name}.pdf'

    # Format the current time without milliseconds
    current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Create a new PDF file
    pdf_writer = PyPDF2.PdfWriter()

    # Add a blank page to the PDF
    pdf_writer.add_blank_page(width=612, height=792)  # Standard US Letter size in points (8.5 x 11 inches)

    # Create a canvas object to draw on the PDF
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Calculate x-coordinate for centering
    text_width1 = c.stringWidth("Report Results")
    x_coordinate1 = (letter[0] - text_width1) / 2

    text_width2 = c.stringWidth("Motherboard Under Test")
    x_coordinate2 = (letter[0] - text_width2) / 2

    text_width3 = c.stringWidth("Current Time: " + current_time_str)
    x_coordinate3 = (letter[0] - text_width3) / 2

    text_width4 = c.stringWidth("Current User: " + current_user)
    x_coordinate4 = (letter[0] - text_width4) / 2

    # Write "Report Results" at the top centered horizontally
    c.drawString(x_coordinate1, 750, "Report Results")
    c.drawString(x_coordinate2, 730, "Unit Under Test")
    c.drawString(x_coordinate3, 710, "Current Time: " + current_time_str)
    c.drawString(x_coordinate4, 690, "Current User: " + current_user)

    # Calculate x-coordinate for centering images
    image_width1 = 480  # Assuming the width of images is 320

    image_width2 = 240

    image_x_coordinate = (letter[0] - image_width1) / 2

    # Insert the images onto the canvas, centered horizontally
    c.drawImage(image_path1, image_x_coordinate, 300, width=image_width1, height=image_width1 * .75)

    c.drawString(x_coordinate4, 280, "Comparison Result")

    c.drawImage(image_path2, image_x_coordinate, 80, width=image_width2, height=image_width2 * .75)
    c.drawImage(image_path3, (image_x_coordinate * 5) - 20, 80, width=image_width2, height=image_width2 * .75)

    c.drawString(image_x_coordinate * 2 + 12, 65, "Unit Under Test")
    c.drawString(((image_x_coordinate * 5) - 20) + 73, 65, "Reference Image")

    # Save the canvas to the PDF file
    c.save()

    print(f"Image inserted into PDF: {output_filename}")
