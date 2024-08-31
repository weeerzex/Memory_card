from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QListWidget, QListView, QListWidgetItem, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QLabel, QPushButton, QSpinBox
app = QApplication([])

#віджети
menu_btn = QPushButton('Меню')
sleep_btn = QPushButton('Відпочити')
time_sleep = QSpinBox()
time_sleep.setValue(30)
okun_btn =QPushButton('Відповісти')
okun_lb = QLabel('###')

#пвнель з відповідями
RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()
rdbt_1 = QRadioButton('###')
rdbt_2 = QRadioButton('###')
rdbt_3 = QRadioButton('###')
rdbt_4 = QRadioButton('###')
RadioGroup.addButton(rdbt_1)
RadioGroup.addButton(rdbt_2)
RadioGroup.addButton(rdbt_3)
RadioGroup.addButton(rdbt_4)

#Панель з результатами
ResultGroupBox = QGroupBox('Результат тесту')
result_lb = QLabel('#')
result_true_lb = QLabel('#')

#розміщення
layaout_an1 = QHBoxLayout()
layaout_an2 = QVBoxLayout()
layaout_an3 = QVBoxLayout()

layaout_an2.addWidget(rdbt_1)
layaout_an2.addWidget(rdbt_2)

layaout_an3.addWidget(rdbt_3)
layaout_an3.addWidget(rdbt_4)

layaout_an1.addLayout(layaout_an2)
layaout_an1.addLayout(layaout_an3)
RadioGroupBox.setLayout(layaout_an3)

#Розміщеннярезультату
layaout_res = QVBoxLayout()
layaout_res.addWidget(result_lb, alignment = Qt.Alignment, Qt.AlignTop)
layaout_res.addWidget(result_true_lb, alignment = Qt.AlignHCenter, stretch = 2)
ResultGroupBox.SetLayuot(layaout_res)
ResultGroupBox.hide()

#Розміщення віджетів
layaout_line1 = QHBoxLayout()
layaout_line2 = QHBoxLayout()
layaout_line3 = QHBoxLayout()
layaout_line4 = QHBoxLayout()

layaout_line1.addWidget(menu_btn)
layaout_line1.addStretch(1)
layaout_line1.addWidget(sleep_btn)
layaout_line1.addWidget(time_sleep)

layaout_line2.addWidget(okun_lb)

layaout_line3.addWidget(RadioGroup)
layaout_line3.addWidget(result_lb)

layaout_line4.addStretch(1)
layaout_line4.addWidget(okun_btn, stretch = 2 )
layaout_line4.addStretch(1)

card_layout = QVBoxLayout()
card_layout.addLayout(layaout_line1,stretch = 1)
card_layout.addLayout(layaout_line2,stretch = 2)
card_layout.addLayout(layaout_line3,stretch = 8)
card_layout.addStretch(1)
card_layout.addLayout(layaout_line4,stretch = 1)
card_layout.setSpacing(5)
card_layout.addStretch(1)

#relelt
def show_result():
    RadioGroupBox.hide()
    ResultGroupBox.show()
    okun_btn.setText('Наступне питання')

def show_questions():
    RadioGroupBox.show()
    ResultGroupBox.hide()
    okun_btn.setText('Відповісти')

RadioGroup.setExclusive(False)
rdbt_1.setChecked(False)
rdbt_2.setChecked(False)
rdbt_3.setChecked(False)
rdbt_4.setChecked(False)
RadioGroup.setExclusive(True)

    







