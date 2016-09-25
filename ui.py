# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
from main import getTask
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(469, 276)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.button = QtGui.QPushButton(self.centralWidget)
        self.button.setGeometry(QtCore.QRect(404, 50, 61, 20))
        self.button.setObjectName(_fromUtf8("button"))
        self.buttonOk = QtGui.QPushButton(self.centralWidget)
        self.buttonOk.setGeometry(QtCore.QRect(200, 70, 60, 25))
        self.buttonOk.setObjectName(_fromUtf8("button"))
        self.input = QtGui.QLineEdit(self.centralWidget)
        self.input.setGeometry(QtCore.QRect(10, 50, 391, 20))
        self.input.setObjectName(_fromUtf8("input"))
        self.label_desc = QtGui.QLabel(self.centralWidget)
        self.label_desc.setGeometry(QtCore.QRect(10, 30, 451, 20))
        self.label_desc.setObjectName(_fromUtf8("label_desc"))
        self.output = QtGui.QTextEdit(self.centralWidget)
        self.output.setGeometry(QtCore.QRect(10, 100, 451, 141))
        self.output.setObjectName(_fromUtf8("output"))
        self.label_result = QtGui.QLabel(self.centralWidget)
        self.label_result.setGeometry(QtCore.QRect(10, 80, 54, 12))
        self.label_result.setObjectName(_fromUtf8("label_result"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 469, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getPath)
        QtCore.QObject.connect(self.buttonOk, QtCore.SIGNAL(_fromUtf8("clicked()")), self.changeDB)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        try:
            f = open("path.txt", "r")
        except IOError:
            pass
        else:
            self.input.setText(f.readline())
            f.close()
        MainWindow.setWindowTitle(_translate("MainWindow", "迅雷加速破解", None))
        self.main.setWindowIcon(QtGui.QIcon('ui.ico'))
        self.button.setText(_translate("MainWindow", "浏览", None))
        self.buttonOk.setText(_translate("MainWindow", "加速", None))
        self.label_desc.setText(_translate("MainWindow", "请键入迅雷数据库所在文件或者选择路径，位于迅雷安装路径/Profiles/TaskDb.dat", None))
        self.label_result.setText(_translate("MainWindow", "结果输出", None))
        self.label.setText(_translate("MainWindow", "使用方法：先进入迅雷建立下载任务，等待违禁提示后关闭迅雷运行本程序", None))

    def error(self, string):
        box = QtGui.QMessageBox
        msgBox = box(box.Warning, u"错误", string,box.Ok)
        msgBox.exec_()
        return

    def ok(self, string):
        box = QtGui.QMessageBox
        msgBox = box(box.Information, u"成功", string,box.Ok)
        msgBox.exec_()
        return

    def getPath(self):
        absolute_path = QFileDialog.getOpenFileName(self.main, 'Open file', '.', "Dat files (*.dat)")
        if absolute_path.split('/')[-1] != "TaskDb.dat":
            self.error(u"文件名称错误！")
            return
        f = open("path.txt", "w")
        f.write(absolute_path)
        f.close()
        self.input.setText(absolute_path)
        self.changeDB()

    def changeDB(self):
        ans = u"现在正在读取数据库...\n"
        try:
            t, num, flyNum = getTask(str(self.input.text()))
        except Exception, e:
            self.error(str(e))
            return
        self.ok(u"加速成功！")
        ans += "".join(t)
        ans += u"执行完毕，现在总共有%s个任务在下载中,新加速了%s个任务\n" % (num, flyNum)
        self.output.setText(ans)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

