# -*- coding: utf-8 -*-
import time
from threading import Thread

from PySide6.QtWidgets import QApplication, QMainWindow
# PySide6-uic filetoword.ui -o filetoword.py
# from ui_demo import Ui_Demo
# from task import add
from filetoword import Ui_Form
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

    def band(self):
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)

        self.ui.fileinput.clicked.connect(self.getfilepath)
        self.ui.fileoutput.clicked.connect(self.getfilepath2)
        self.ui.refreshButton.clicked.connect(self.refresh)
#        self.ui.searchButton.clicked.connect(self.search)
        self.ui.recognize.clicked.connect(self.recognize_deal)

    def getfilepath(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        NewWindow = QDialog()
        FileDialog = QFileDialog(NewWindow)
        FileDirectory = FileDialog.getExistingDirectory(NewWindow, "标题")  # 选择目录，返回选中的路径
        self.ui.filepath.setPlainText(FileDirectory)
#        self.ui.filepath_2.setPlainText(FileDirectory.split('\\')[0:-1])
    def getfilepath2(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        NewWindow = QDialog()
        FileDialog = QFileDialog(NewWindow)
        FileDirectory = FileDialog.getExistingDirectory(NewWindow, "标题")  # 选择目录，返回选中的路径
        self.ui.filepath_2.setPlainText(FileDirectory)
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
    def get_access_token(self):
        url = 'https://aip.baidubce.com/oauth/2.0/token'
        data = {
            'grant_type': 'client_credentials',  # 固定值
            'client_id': '7qGKEXsdUbeg5l5Hmsbl057t',  # 在开放平台注册后所建应用的API Key
            'client_secret': 'MpC7Urn6p8HUL1Wv6dqs4GZbz4L6N9ci'  # 所建应用的Secret Key
        }
        res = requests.post(url, data=data)
        res = res.json()
        print(res)
        access_token = res['access_token']
        return access_token

    def general_word(self,r_path, w_path):
        # 通用文字识别接口url
        general_word_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
        # 获取执行路径
        # path = os.getcwd()
        # 二进制方式打开图片文件
        f = open(r_path, 'rb')
        img = base64.b64encode(f.read())
        print(img)
        params = {"image": img,
                  "language_type": "CHN_ENG"}
        access_token = self.get_access_token()
        request_url = general_word_url + "?access_token=" + access_token
        print(request_url)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        # print(response)
        # res = response.json()
        if response:
            res = response.json()["words_result"]
            print(res)
            file_name = w_path
            with open(file_name, 'w', encoding='utf-8') as f:
                for j in res:
                    print(j["words"])
                    f.write(j["words"] + "\n")

    def recognize_deal(self):
        NewWindow = QDialog()
        MessageBox = QMessageBox()
        Ret = MessageBox.question(NewWindow, "警告", "文件将按文件路径形式进行处理,请确定文件列表是否正确")  # Critical对话框
        print(str(Ret))
        if str(Ret) == "StandardButton.Yes":
            path = self.ui.filepath.toPlainText()
            pathout = self.ui.filepath_2.toPlainText()

            self.ui.output_files.setPlainText("")
            for index,filename in enumerate(os.listdir(path)):
                # nn = len(os.listdir(path))
                # print(index,nn)
                # progress = index * 100 // (nn-1)
                # self.set_progress_bar(progress)
                expand_names= filename.split(".")[-1]
                if expand_names == "jpg" or expand_names == "png" or expand_names == "JPG" or expand_names == "jpeg":
                    srcFile = os.path.join(path, filename)
                    dstFile = os.path.join(pathout, time_str + "." + timename)
                self.ui.output_files.append("dealing "+ filename+ " "+"to"+" "+ time_str + "." + timename)
                self.general_word()

if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出
