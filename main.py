from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget, QScrollArea, QHBoxLayout
from PySide6.QtCore import Qt
import sys


class App:
    count_text_edit_showup_times = 1
    def __init__(self):
        self.ui = QUiLoader().load("main.ui")

        self.QScrollArea = QScrollArea(parent=self.ui)
        self.QScrollArea.setGeometry(350, 100, 300, 200)
        self.widget = QWidget()
        # self.widget.setGeometry(350, 70, 300, 500)
        self.layout = QVBoxLayout(self.widget)
        self.layout.setAlignment(Qt.AlignTop)
        self.ui.pushButton.clicked.connect(self.create_new_input_box)
        self.ui.show()


    def create_new_input_box(self):
        self.count_text_edit_showup_times += 2
        textEdit_x = QTextEdit()
        textEdit_x.setObjectName(f"{self.count_text_edit_showup_times}")
        textEdit_x.setMaximumSize(80, 30)
        textEdit_y = QTextEdit()
        textEdit_y.setMaximumSize(80, 30)
        temp_widget = QWidget()
        temp_layout = QHBoxLayout(temp_widget)
        temp_layout.addWidget(textEdit_x)
        temp_layout.addWidget(textEdit_y)
        temp_layout.setAlignment(Qt.AlignTop)

        # print("12:",textEdit_x.toPlainText())


        self.layout.addWidget(temp_widget)
        self.layout.setSpacing(2)
        self.QScrollArea.setWidget(self.widget)
        self.QScrollArea.setWidgetResizable(True)


    # def






if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = App()
    sys.exit(app.exec())
