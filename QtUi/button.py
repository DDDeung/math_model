# FileName : main.py
# Author   : Adil
# DateTime : 2018/8/13 10:18
# SoftWare : PyCharm

import sys
import MyWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = MyWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())