import sys
from PySide6 import QtCore, QtWidgets, QtGui
import ui_login  # 导入ui_login.py
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtWidgets import QApplication, QDialog
# PySide6-uic demo.ui -o ui_demo.py
# from ui_demo import Ui_Demo
class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # 在此创建窗体上的部件

        # 使用UI文件创建部件，如果有的话
        self.ui = ui_xxxx.Ui_Dialog()
        self.ui.setupUi(self)
        self.band()

    def band(self):
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)

        self.ui.fileget.clicked.connect(print(123))#self.getfilepath

    def getfilepath(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        NewWindow = QDialog()
        FileDialog = QFileDialog(NewWindow)
        FileDirectory = FileDialog.getExistingDirectory(NewWindow, "标题")  # 选择目录，返回选中的路径
        print(FileDirectory)
        ui.filepath.setPlainText(FileDirectory)
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        ui = ui_login.Ui_Form()  # 实例化UI对象
        ui.setupUi(self)  # 初始化
        ui.filepath.setPlainText("123")




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())