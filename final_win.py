# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
class Final_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_windth, win_heidht)
        self.move(win_x, win_y)
    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.p_line = QVBoxLayout
        self.p_line.addWidgetget(self.ntk1, alignment = QtAlignCenter)
        self.p_line.addWidgetget(self.ntk2, alignment = QtAlignCenter)
        self.setLayout(self.p_line)
    def results(self):
        self.index = (4*(int(self.Toht.t1) + (int(self.Toht.t1) + (int(self.Toht.t1))-200)/10)
        if self.Toht.age >= 15:
            if self.index >=15:
                return txt_res1
            elif self.index >= 11 and self.index <= 14.9:
                return txt_res2
            elif self.index >= 6 and self.index <= 10.9:
                return txt_res3
            elif self.index >= 0.5 and self.index <= 5.9:
                return txt_res4
            elif self.index >= 0.4:
                return txt_res5
        if self.Toht.age >= 13 and Toht.age <= 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index >= 12.5 and self.index <= 16.4:
                return txt_res2
            elif self.index >= 7.5 and self.index <= 12.4:
                return txt_res3
            elif self.index >= 2 and self.index <= 7.4:
                return txt_res4
            elif self.index >= 1.9:
                return txt_res5
        if self.Toht.age >= 11 and Toht.age <= 12:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14 and self.index <= 17.9:
                return txt_res2
            elif self.index >= 9 and self.index <= 13.9:
                return txt_res3
            elif self.index >= 3.5 and self.index <= 8.9:
                return txt_res4
            elif self.index >= 3.4:
                return txt_res5
        if self.Toht.age >= 9 and Toht.age <= 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >= 15.5 and self.index <= 19.4:
                return txt_res2
            elif self.index >= 10.5 and self.index <= 15.4:
                return txt_res3
            elif self.index >= 5 and self.index <= 10.4:
                return txt_res4
            elif self.index >= 4.9:
                return txt_res5
        if self.Toht.age >= 7 and Toht.age <= 8:
            if self.index >= 21:
                return txt_res1
            elif self.index >= 17 and self.index <= 20.9:
                return txt_res2
            elif self.index >= 12 and self.index <= 16.9:
                return txt_res3
            elif self.index >= 6.5 and self.index <= 11.9:
                return txt_res4
            elif self.index >= 6.4:
                return txt_res5
        if self.Toht.age < 7:
            self.index = 0
            return 'нет данных для такого возраста'

app = QApplication([])
fw = Final_win()
app.exe_()