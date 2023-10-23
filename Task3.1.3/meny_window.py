from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLineEdit, QButtonGroup, QGroupBox, QWidget, QPushButton, QLabel, QVBoxLayout,  QRadioButton, QHBoxLayout, QMessageBox, QSpinBox)
card_width, card_height = 500, 600

app = QApplication([])
menu_win = QWidget()
menu_win.resize(card_width,card_height)


main_layot = QHBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()
layout4 = QHBoxLayout()
layout6 = QHBoxLayout()
layout7 = QHBoxLayout()
layout8 = QHBoxLayout()

q = QLabel("Введіть запитання")
right_asn =QLabel("Введіть вірну відповідь")
right_wrong =QLabel("Введіть першу хибну відповідь")
right_wrong =QLabel("Введіть другу хибну відповідь")
right_wrong =QLabel("Введіть третю хибну відповідь")




text1 = QLineEdit()
text2 = QLineEdit()
text3 = QLineEdit()
text4 = QLineEdit()
text5 = QLineEdit()

btn1 = QPushButton()
btn2 = QPushButton()
btn3 = QPushButton()


line = QLabel("Статистика")





text_result = QVBoxLayout()
text_result.addWidget(q)
text_result.addWidget(right_asn)
text_result.addWidget(right_wrong)
text_result.addWidget(right_wrong)
text_result.addWidget(right_wrong)




text_no = QVBoxLayout()
text_no.addWidget(text1)
text_no.addWidget(text2)
text_no.addWidget(text3)
text_no.addWidget(text4)
text_no.addWidget(text5)



Hline = QHBoxLayout()
Hline.addLayout(text_result)
Hline.addLayout(text_no)

btn_back = QPushButton("Назад")
btn_add_quest = QPushButton("Додати запитвння")
btn_clear = QPushButton("Очистити")
hl_button = QHBoxLayout()
hl_buttons = QHBoxLayout()
hl_button.addWidget(btn_add_quest)
hl_button.addWidget(btn_clear)

vl_res = QVBoxLayout()
vl_res.addLayout(Hline)
vl_res.addWidget(line)
vl_res.addWidget(btn_back)
vl_res.addWidget(text_no)

menu_win.setLayout(vl_res)



app.exec()