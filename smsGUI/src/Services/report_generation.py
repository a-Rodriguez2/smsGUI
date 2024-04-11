import PyPDF2
from PyQt5.QtWidgets import QFileDialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def create_pdf_with_image(image_path1, image_path2, save_report,
                          ppid, current_user, name, worker_id, station_number):
    """

    :param image_path1: Image of result comparison.
    :param image_path2: Image of Motherboard Unit Under Test.
    :param save_report: Decides whether 'save' or 'save as'.
    :param ppid: Motherboard identifier.
    :param current_user: OS system username.
    :param name: Name decided by user.
    :param worker_id: Worker ID decided by user.
    :param station_number: Station Number decided by user.
    :return: None

    """

    # initialize report file name
    output_filename = None

    # determine and format time
    current_time = datetime.now()
    current_time_name = current_time.strftime('%Y-%m-%d_%H_%M_%S')
    current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # report 'save' operation
    if save_report == 1:
        output_filename = f'Reports\\Report_{current_time_name}.pdf'
    # report 'save as' operation
    if save_report == 0:
        options = QFileDialog.Options()
        output_filename, _ = QFileDialog.getSaveFileName(None, "Save PDF As", "Reports", "PDF Files (*.pdf)", options=options)

    # check that user has decided a file name before creating the pdf
    if output_filename:
        # Create a new PDF file
        pdf_writer = PyPDF2.PdfWriter()

        # Add a blank page to the PDF
        pdf_writer.add_blank_page(width=612, height=792)  # Standard US Letter size in points (8.5 x 11 inches)

        # Create a canvas object to draw on the PDF
        c = canvas.Canvas(output_filename, pagesize=letter)

        # Determine coordinates for text and images
        text1 = f'Report Results:  {current_time_str}'
        text_width1 = c.stringWidth(text1)
        x_coordinate1 = (letter[0] - text_width1) / 2
        c.drawString(x_coordinate1, 760, text1)

        text2 = f'Unit Under Test: {ppid}'
        text_width2 = c.stringWidth(text2)
        x_coordinate2 = (letter[0] - 480) / 2
        c.drawString(x_coordinate2, 730, text2)

        text3 = f'Current User: {current_user} ({name})'
        text_width3 = c.stringWidth(text3)
        x_coordinate3 = (letter[0] - text_width3) / 2
        c.drawString(x_coordinate2, 710, text3)

        text4 = f'Worker ID: {worker_id}'
        text_width4 = c.stringWidth(text4)
        c.drawString(x_coordinate2, 690, text4)

        text5 = f'Station Number: {station_number}'
        text_width5 = c.stringWidth(text5)
        c.drawString(x_coordinate2, 670, text5)

        # Define image dimensions before writing to pdf
        image_width = 420
        # 16:9 aspect ratio
        image_height = (image_width * 0.75)
        image_x_coordinate = (letter[0] - image_width) / 2

        c.drawImage(image_path1, image_x_coordinate, 340, width=image_width, height=image_height)
        c.drawImage(image_path2, image_x_coordinate, 10, width=image_width, height=image_height)

        text6 = 'Comparison Result'
        text_width6 = c.stringWidth(text6)
        x_coordinate6 = (letter[0] - text_width6) / 2
        c.drawString(x_coordinate6, 350, text6)

        text7 = 'Unit Under Test'
        text_width7 = c.stringWidth(text7)
        x_coordinate7 = (letter[0] - text_width7) / 2
        c.drawString(x_coordinate7, 20, text7)

        # Save the canvas to the PDF file
        c.save()

    else:
        pass
