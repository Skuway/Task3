from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QButtonGroup, QGroupBox, QWidget, QPushButton, QLabel, QVBoxLayout,  QRadioButton, QHBoxLayout, QMessageBox, QSpinBox)
card_width, card_height = 500, 600
app = QApplication([])
main_win = QWidget()

main_win.resize(card_width, card_height)
main_win.move(300,300)
main_win.show()
main_win.setWindowTitle("Memory card")


btn_sleep = QPushButton("Відпочити")
box_minutes = QSpinBox()
box_minutes.setValue(30)

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відповідь")
lb_quest = QLabel('')

RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()

rbtn_ans1 = QRadioButton("1")
rbtn_ans2 = QRadioButton("2")
rbtn_ans3 = QRadioButton("3")
rbtn_ans4 = QRadioButton("4")

RadioGroup.addButton(rbtn_ans1)
RadioGroup.addButton(rbtn_ans2)
RadioGroup.addButton(rbtn_ans3)
RadioGroup.addButton(rbtn_ans4)

ansgroup = QGroupBox('Результати теста')
lb_resulr = QLabel('')
lb_correct = QLabel('')



Layout_ans1 = QHBoxLayout()
Layout_ans2 = QVBoxLayout()
Layout_ans3 = QVBoxLayout()
Layout_ans2.addWidget(rbtn_ans1,)
Layout_ans2.addWidget(rbtn_ans2,)
Layout_ans3.addWidget(rbtn_ans3,)
Layout_ans3.addWidget(rbtn_ans4,)
Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)
RadioGroupBox.setLayout(Layout_ans1)

Layout_res = QVBoxLayout()
Layout_res.addWidget(lb_resulr, alignment=(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop))
Layout_res.addWidget(lb_correct, alignment= Qt.AlignmentFlag.AlignHCenter, stretch=2 )
ansgroup.setLayout(Layout_res)
ansgroup.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()
layout_line1.addWidget(btn_menu)

layout_line1.addStretch(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_minutes)

layout_line1.addWidget(QLabel("хвилин"))

layout_line2.addWidget(lb_quest, alignment=(
    Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(ansgroup)



layout_line4.addStretch(1)
layout_line4.addWidget(btn_rest)
layout_line4.addStretch(1)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch= 2)

layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.setSpacing(5)
main_win.setLayout(layout_card)
layout_card.addStretch(1)


def show_result():
    RadioGroupBox.hide
    ansgroup.show
    btn_rest.setText("Наступне питання")


def show_qestion():
    RadioGroupBox.show()
    ansgroup.hide()
    btn_rest.setText("Відповісти")
    rbtn_ans1.setChecked(False)
    rbtn_ans1.setChecked(False)
    rbtn_ans1.setChecked(False)
    rbtn_ans1.setChecked(False)
    RadioGroup.setExclusive(True)




main_win.show()
app.exec()














