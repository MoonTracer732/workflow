# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QProgressBar, QPushButton, QSizePolicy,
    QSplitter, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(710, 547)
        Form.setAutoFillBackground(True)
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 410, 601, 31))
        self.progressBar.setValue(24)
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(60, 30, 601, 31))
        self.splitter.setOrientation(Qt.Horizontal)
        self.filepath = QTextEdit(self.splitter)
        self.filepath.setObjectName(u"filepath")
        self.splitter.addWidget(self.filepath)
        self.fileget = QPushButton(self.splitter)
        self.fileget.setObjectName(u"fileget")
        font = QFont()
        font.setPointSize(11)
        self.fileget.setFont(font)
        self.splitter.addWidget(self.fileget)
        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.splitter.addWidget(self.pushButton)
        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(60, 80, 601, 321))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.listed_files = QTextEdit(self.splitter_2)
        self.listed_files.setObjectName(u"listed_files")
        self.splitter_2.addWidget(self.listed_files)
        self.changed_files = QTextEdit(self.splitter_2)
        self.changed_files.setObjectName(u"changed_files")
        self.splitter_2.addWidget(self.changed_files)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 460, 599, 28))
        self.pushButton_2.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.filepath.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.fileget.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u9009\u62e9", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d\u8f6c\u6362", None))
    # retranslateUi

