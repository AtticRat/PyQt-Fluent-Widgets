# coding:utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

from qfluentwidgets import LineEdit, PushButton, TextEdit


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.lineEdit = LineEdit('', self)
        self.button = PushButton('按钮', self)
        self.textEdit = TextEdit(self)

        self.resize(500, 500)
        self.textEdit.move(110, 200)
        self.lineEdit.move(110, 50)
        self.button.move(320, 52)
        
        self.lineEdit.resize(200, 33)
        self.lineEdit.setClearButtonEnabled(True)


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()