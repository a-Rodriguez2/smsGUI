import os.path

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import cv2
import numpy
import datetime

class VideoThread(QThread):
    # signal to update video frame label
    update_pixmap_signal = pyqtSignal(numpy.ndarray)
    finished_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # boolean for starting and stopping thread
        self.run_flag = True
        self.cap = cv2.VideoCapture(0)
        # comment-out to manipulate camera settings
        # self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,3000)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,4000)
        # self.cap.set(28,72)

    def run(self):
        # while allowed to run, read video frame and emit signal to update label
        while self.run_flag:
            ret, frame = self.cap.read()
            if ret:
                self.update_pixmap_signal.emit(frame)
        # when no longer running, release video capture and emit signal to complete video capture
        self.cap.release()
        self.finished_signal.emit()

    def capture_frame(self, save_file):
        ret, frame = self.cap.read()
        if ret:
            # file 'save as' operation
            if not save_file:
                filename, _ = QFileDialog.getSaveFileName(None, "Save Image", "", "Images (*.png *.jpg *.jpeg)")
                if filename:
                    cv2.imwrite(filename, frame)
                    QMessageBox.information(None, 'Success', f'Frame captured and saved as {filename} successfully!')
                else:
                    QMessageBox.warning(None, 'Error', 'Did not capture frame.')
            # file 'save' operation
            else:
                current_datetime = datetime.datetime.now()
                current_date = current_datetime.strftime('%m-%d-%Y')
                current_time = current_datetime.strftime('%H-%M-%S')
                image_name = f'capture_date_{current_date}_time_{current_time}.png'
                image_path = os.path.join('GUI Images', image_name)
                cv2.imwrite(image_path, frame)
                QMessageBox.information(None, 'Success', f'Frame captured and saved as {image_name} successfully!')

    def stop(self):
        self.run_flag = False
        # wait for thread to completely stop
        self.wait()
