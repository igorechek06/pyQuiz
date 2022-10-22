from typing import Callable

import requests
from PIL import Image
from PyQt5 import QtCore, QtWidgets

import models as m


class DownloadImage(QtCore.QRunnable):
    widget: QtWidgets.QLabel
    url: str

    def __init__(self, widget: QtWidgets.QLabel, url: str) -> None:
        super().__init__()
        self.widget = widget
        self.url = url

    def run(self) -> None:
        image = Image.open(requests.get(self.url, stream=True).raw)
        self.widget.setPixmap(image.toqpixmap())
