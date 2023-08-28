# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,QVBoxLayout,QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def result(self):
        '''if self.exp.age < 7:
            self.abc = 0
            return 'Ошибка' '''
        self.index = (4*(int(self.exp.test1) + int(self.exp.test2) + int(self.exp.test3))- 200)/10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1 
            elif 17 <= self.index < 21:
                return txt_res2
            elif 12 <= self.index < 17:
                return txt_res3
            elif 6.5 <= self.index < 12:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1 
            elif 15.5 <= self.index < 19.5:
                return txt_res2
            elif 10.5 <= self.index < 15.5:
                return txt_res3
            elif 5 <= self.index < 10.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1 
            elif 14 <= self.index < 18:
                return txt_res2
            elif 9 <= self.index < 14:
                return txt_res3
            elif 3.5 <= self.index < 9:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1 
            elif 12.5 <= self.index < 16.5:
                return txt_res2
            elif 7.5 <= self.index < 12.5:
                return txt_res3
            elif 2 <= self.index < 7.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1 
            elif 11 <= self.index < 15:
                return txt_res2
            elif 6 <= self.index < 11:
                return txt_res3
            elif 0.5 <= self.index < 6:
                return txt_res4
            else:
                return txt_res5
    def initUI(self):
        res = str(self.result())
        indx = self.index
        self.instruction = QLabel(txt_workheart + res)
        self.hello_text = QLabel(txt_index + str(indx))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_y, win_x)
        self.resize(win_width, win_height)