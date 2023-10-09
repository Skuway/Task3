from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QGroupBox, QWidget, QPushButton, QLabel, QVBoxLayout,  QRadioButton, QHBoxLayout, QMessageBox,QSpinBox
card_width, card_height = 500, 600
app = QApplication([])
main_win = QWidget()

btn_sleep = QPushButton("Відпочити")
box_minutes = QSpinBox()
box_minutes.setValue(30)

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відповідь")

RadioGroupBox = QGroupBox
RadioGroup = QButtonGroup()

rbtn_ans1 = QRadioButton("1")
rbtn_ans2 = QRadioButton("2")
rbtn_ans3 = QRadioButton("3")
rbtn_ans4 = QRadioButton("4")

RadioGroup.addButton(rbtn_ans1)
RadioGroup.addButton(rbtn_ans2)
RadioGroup.addButton(rbtn_ans3)
RadioGroup.addButton(rbtn_ans4)

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QVBoxLayout()
Layout_ans3 = QVBoxLayout()
Layout_ans2.addWidget(rbtn_ans1,rbtn_ans2)
Layout_ans3.addWidget(rbtn_ans3,rbtn_ans4)
Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)
RadioGroupBox.setLayout(Layout_ans1)



main_win.resize(card_width, card_height)
main_win.move(300,300)
main_win.show()
main_win.setWindowTitle("Memory card")











app.exec_()