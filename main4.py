import sys
from PySide6 import QtCore, QtWidgets, QtGui
import ui_login  # 导入ui_login.py


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        ui = ui_login.Ui_Form()  # 实例化UI对象
        ui.setupUi(self)  # 初始化



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())