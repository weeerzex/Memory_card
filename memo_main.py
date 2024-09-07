from memo_card_layout import(
    app, layaut card,lb_Question, lb_Correct,
    lb Result, rbtn_1, rbtn_2, rbtn_3, rbtn_4, bth ok,
    show _result, show _question
)
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle

card_width, card_heihgt = 600, 900
text_wrong = 'Неправильно'
text_correct = 'Правильно'

frm_question = 'в якому році Україна стала незалежною?'
frm_right = '1991'
frm_wrong1 = '1990'
frm_wrong2 = '1994'
frm_wrong3 = '1993'

radiolist = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radiolist)
answer = radiolist[0]
wrong_answer1, wrong_answer2, wrong_answer3 = radiolist[1], radiolist[2], radiolist[3]

def show_data():
    lb_Questiot.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)

def check_result():
    correct = answer.isChecked()
    if correct:
        lb_Result.setText(text_correct)
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:
            lb_Result.SetText(text_wrong)
            show_result()

    def click_ok():
        if btn_Ok != 'Наступне питання':
            check_result()

win_card = QWidget()
win_card.resize(card_width, card_heihgt)
win_card.move(300, 300)
win_card.setWindowTitle('Memory card')

win_card.setLayout(layout_card)
show_data()
show_question()
btn_Ok.Clicked.connect(click_ok)

win_card.show()
app.exec_()