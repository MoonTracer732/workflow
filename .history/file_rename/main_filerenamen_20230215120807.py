# -*- coding: utf-8 -*-
import time
from threading import Thread

from PySide6.QtWidgets import QApplication, QMainWindow
# PySide6-uic demo.ui -o ui_demo.py
# from ui_demo import Ui_Demo
# from task import add
from ui_login import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QMessageBox
import time
import os.path
# from Signal import my_signal


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()  # UI类的实例化()
        self.ui.setupUi(self)
        self.band()

        self.set_progress_bar(0)
    def band(self):
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)

        self.ui.fileget.clicked.connect(self.getfilepath)
        self.ui.pushButton.clicked.connect(self.refresh)
        self.ui.pushButton_2.clicked.connect(self.rename)
    def getfilepath(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        NewWindow = QDialog()
        FileDialog = QFileDialog(NewWindow)
        FileDirectory = FileDialog.getExistingDirectory(NewWindow, "标题")  # 选择目录，返回选中的路径
        self.ui.filepath.setPlainText(FileDirectory)
    def refresh(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        path = self.ui.filepath.toPlainText()
        if os.path.isdir(path):
            # 判断当前文件路径是否存在
            self.ui.listed_files.setPlainText("")
            self.ui.listed_files.append("file list is:")
            for filename in os.listdir(path):
                curr_path = os.path.join(path, filename)
                self.ui.listed_files.append(curr_path)
        else:
            self.ui.listed_files.setPlainText("There is no such filepath!!!")
    def set_progress_bar(self, progress: int):
        self.ui.progressBar.setValue(progress)
    def rename(self):
        NewWindow = QDialog()
        MessageBox = QMessageBox()
        Ret = MessageBox.question(NewWindow, "警告", "文件将按时间形式进行重命名,请确定文件列表是否正确")  # Critical对话框
        print(str(Ret))
        if str(Ret) == "StandardButton.Yes":
            path = self.ui.filepath.toPlainText()
            self.ui.changed_files.setPlainText("")
            for index,filename in enumerate(os.listdir(path)):
                nn = len(os.listdir(path))
                print(index,nn)
                progress = index * 100 // (nn-1)
                self.set_progress_bar(progress)
                curr_path = os.path.join(path, filename)
                filemt = time.localtime(os.stat(curr_path).st_mtime)
                time_str = time.strftime("%y-%m-%d_%H_%M_%a", filemt)
                timename = filename.split(".")[-1]
                srcFile = os.path.join(path, filename)
                dstFile = os.path.join(path, time_str + "." + timename)
                self.ui.changed_files.append("dealing "+ filename+ " "+"to"+" "+ time_str + "." + timename)
                if os.path.exists(srcFile):
                    os.rename(srcFile, dstFile)
if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出
