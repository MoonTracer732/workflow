# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filetoword.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QSplitter,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(738, 585)
        self.listed_files = QTextEdit(Form)
        self.listed_files.setObjectName(u"listed_files")
        self.listed_files.setGeometry(QRect(49, 179, 261, 301))
        self.output_files = QTextEdit(Form)
        self.output_files.setObjectName(u"output_files")
        self.output_files.setGeometry(QRect(339, 129, 311, 351))
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(50, 40, 601, 31))
        self.splitter.setOrientation(Qt.Horizontal)
        self.filepath = QTextEdit(self.splitter)
        self.filepath.setObjectName(u"filepath")
        self.splitter.addWidget(self.filepath)
        self.fileinput = QPushButton(self.splitter)
        self.fileinput.setObjectName(u"fileinput")
        font = QFont()
        font.setPointSize(11)
        self.fileinput.setFont(font)
        self.splitter.addWidget(self.fileinput)
        self.refreshButton = QPushButton(self.splitter)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setFont(font)
        self.splitter.addWidget(self.refreshButton)
        self.search = QTextEdit(Form)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(50, 130, 178, 29))
        self.searchButton = QPushButton(Form)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(240, 130, 75, 28))
        self.searchButton.setFont(font)
        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(50, 80, 601, 31))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.filepath_2 = QTextEdit(self.splitter_2)
        self.filepath_2.setObjectName(u"filepath_2")
        self.splitter_2.addWidget(self.filepath_2)
        self.fileoutput = QPushButton(self.splitter_2)
        self.fileoutput.setObjectName(u"fileoutput")
        self.fileoutput.setFont(font)
        self.splitter_2.addWidget(self.fileoutput)
        self.recognize = QPushButton(self.splitter_2)
        self.recognize.setObjectName(u"recognize")
        self.recognize.setFont(font)
        self.splitter_2.addWidget(self.recognize)

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
        self.fileinput.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u6587\u4ef6\u8def\u5f84", None))
        self.refreshButton.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.search.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u8bf7\u5728\u6b64\u952e\u5165\u641c\u7d22\u5185\u5bb9</span></p></body></html>", None))
        self.searchButton.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.filepath_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.fileoutput.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u6587\u4ef6\u8def\u5f84", None))
        self.recognize.setText(QCoreApplication.translate("Form", u"\u6587\u5b57\u8bc6\u522b", None))
    # retranslateUi

