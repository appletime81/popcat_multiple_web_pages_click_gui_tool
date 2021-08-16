from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QTableWidgetItem
import sys
import win32api
import win32con
from ctypes import *
import time
import keyboard


def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)


class App:
    count = 0
    def __init__(self):
        self.ui = QUiLoader().load("main.ui")
        self.ui.setWindowTitle("Taiwan No.1")
        self.ui.add_coord_btn.clicked.connect(self.create_coord)
        self.ui.start_btn.clicked.connect(self.start_click)
        self.ui.show()

    def create_coord(self):
        self.count += 1
        self.ui.table.setRowCount(self.count)
        self.ui.table.setColumnCount(2)
        for i in range(self.count):
            for j in range(2):
                try:
                    self.ui.table.setItem(i, j, QTableWidgetItem(str(self.ui.table.item(i, j).text())))
                except:
                    pass
        self.ui.table.setHorizontalHeaderLabels(["X", "Y"])

    def start_click(self):
        x = []
        y = []
        for i in range(self.count):
            for j in range(2):
                if j == 0:
                    try:
                        x.append(int(self.ui.table.item(i, j).text()))
                    except:
                        pass
                else:
                    try:
                        y.append(int(self.ui.table.item(i, j).text()))
                    except:
                        pass
        while True:
            if keyboard.is_pressed("q"):
                break
            else:
                for x_coord, y_coord in zip(x, y):
                    windll.user32.SetCursorPos(x_coord, y_coord)
                    clickLeftCur()
                    time.sleep(0.001)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = App()
    sys.exit(app.exec())

# pyinstaller -F -w --icon "popcat_background.ico" "main.py" -n "TaiwanWillWin"

