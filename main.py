from ast import Index

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from iterator import *


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.label = None
        self.setWindowTitle("Viewer")
        self.setFixedSize(QSize(720, 400))

        self.set_welcome_menu()

    def set_welcome_menu(self) -> None:
        """
        Create welcome meny
        :return: none
        """
        self.path = None
        self.images = None

        button_open = QPushButton("Open file with images")
        button_open.setFixedSize(200, 50)
        button_open.setStyleSheet("background-color: lightblue; color: black;")
        button_open.clicked.connect(self.select_csv)

        layout_button = QVBoxLayout()
        layout_button.addStretch()
        layout_button.addWidget(button_open, alignment=Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        container.setLayout(layout_button)
        self.setCentralWidget(container)

    def images_menu(self) -> None:
        """
        Create meny with images
        :return: None
        """
        self.label = QLabel()
        button_next_image = QPushButton("Next image")
        button_next_image.setFixedSize(110,25)
        button_next_image.setStyleSheet("background-color: lightblue; color: black")
        button_close = QPushButton("Exit")
        button_close.setFixedSize(100,25)
        button_close.setStyleSheet("background-color: lightblue; color: black")

        button_next_image.clicked.connect(self.next_image)
        button_close.clicked.connect(self.set_welcome_menu)


        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button_next_image, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button_close, alignment=Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.next_image()

    def select_csv(self) -> None:
        """
        Meny to select csv file
        :return: None
        """
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            ".",
            "CSV-like files (*.csv)"
        )
        if filename:
            self.path = filename
            self.images_iterator()
            self.images_menu()

    def images_iterator(self) -> None:
        """
        Create images iterator
        :return: None
        """
        self.images = iter(ImageIterator(self.path))

    def next_image(self) -> None:
        """
        Wrapper for images iterator.
        :return:
        """
        def get_pixmap():
            try:
                return QPixmap(next(self.images))
            except StopIteration:
                return QPixmap()

        pixmap = get_pixmap()
        if pixmap.isNull():
            return
        pixmap = pixmap.scaled(700, 700, Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(pixmap)


def main():
    application = QApplication([])
    window = MainWindow()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()
