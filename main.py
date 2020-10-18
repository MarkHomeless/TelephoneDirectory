import sys
from PyQt5 import QtWidgets, QtCore
from MainWindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        app.exec_()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
