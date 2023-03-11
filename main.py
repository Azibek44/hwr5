from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import sys

def push_button():
    print("Hello Ajibek")

def aaplication():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Python PyQt5")
    window.setGeometry(400,400,400,400)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Hello World")
    main_text.move(150,150)

    main_button = QtWidgets.QPushButton(window)
    main_button.setText("нажми")
    main_button.move(135,190)
    main_button.clicked.connect(push_button)

    window.show()
    sys.exit(app.exec_())
aaplication()    