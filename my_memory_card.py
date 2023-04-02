from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, 
    QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QGroupBox,
    QButtonGroup
    )
from random import shuffle, randint

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Memory Card')
my_win.resize(700, 350)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(
    Question('Государственный язык Австралии?', 'Английский', 'Французский',
    'Австралийский', 'Голландский')
    )
question_list.append(
    Question('Что из перечисленного фрукт?', 'Яблоко', 'Клубника',
    'Банан', 'Картошка')
    )
question_list.append(
    Question('Какая страна находится в Азии?', 'Япония', 'Алжир',
    'Бразилия', 'Гибралтар')
    )

question1 = QLabel('Что из перечисленного дерево?')
button = QPushButton('Ответить')

group = QGroupBox('Варианты ответов')
answer1 = QRadioButton('Вариант 1')
answer2 = QRadioButton('Вариант 2')
answer3 = QRadioButton('Вариант 3')
answer4 = QRadioButton('Вариант 4')
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

layout2.addWidget(answer1, alignment = Qt.AlignCenter)
layout2.addWidget(answer2, alignment = Qt.AlignCenter)
layout3.addWidget(answer3, alignment = Qt.AlignCenter)
layout3.addWidget(answer4, alignment = Qt.AlignCenter)
layout1.addLayout(layout2)
layout1.addLayout(layout3)
group.setLayout(layout1)

AnsGroup = QGroupBox('Результат теста')
result1 = QLabel('Праильно/Неправильно?')
correct = QLabel('Английский')
layout_res = QVBoxLayout()
layout_res.addWidget(result1, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroup.setLayout(layout_res)

layout_one = QHBoxLayout()
layout_two = QHBoxLayout()
layout_three = QHBoxLayout()
layout_one.addWidget(question1, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_two.addWidget(group)
layout_two.addWidget(AnsGroup)

layout_three.addStretch(1)
layout_three.addWidget(button, stretch = 3)
layout_three.addStretch(1)
AnsGroup.hide()
layout_main = QVBoxLayout()
layout_main.addLayout(layout_one, stretch = 2)
layout_main.addLayout(layout_two, stretch = 8)
layout_main.addStretch(1)
layout_main.addLayout(layout_three, stretch = 1)
layout_main.addStretch(1)
layout_main.setSpacing(5)
my_win.setLayout(layout_main)
f = False
def show_result():
    global f, right_answer
    f = True
    group.hide()
    AnsGroup.show()
    #AnsGroup.hide()
    #group.show()
    button.setText('Следующий вопрос')
    correct.setText(right_answer.text())

def show_question():
    global f
    f = False
    #group.hide()
    #AnsGroup.show()
    AnsGroup.hide()
    group.show()
    button.setText('Ответить')
    
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [answer1, answer2, answer3, answer4]
right_answer = answers[0]
wrong1 = answers[1]
wrong2 = answers[2]
wrong3 = answers[3]

def ask(q: Question):
    # shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question1.setText(q.question)
    show_question()

def show_correct(result):
    result1.setText(result)
    show_result()

def check_answer():
    if right_answer.isChecked():
        show_correct('Правильно')
        my_win.score +=1
        print('статистика\n-Всего вопросов:', my_win.total, '\n-Правильных ответов:', my_win.score)
        print('Рейтинг:', (my_win.score / my_win.total * 100), '%')
    else:
        if wrong1.isChecked() or wrong2.isChecked() or wrong3.isChecked():
            show_correct('Неправильно')
            print('Рейтинг:', (my_win.score / my_win.total * 100), '%')
def next_question():
    my_win.total += 1
    print('статистика\n-Всего вопросов:', my_win.total, '\n-Правильных ответов:', my_win.score)
    my_win.cur_question = randint(0, len(question_list) - 1)
    q = question_list[my_win.cur_question]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

my_win.total = 0
my_win.score = 0
my_win.cur_question = -1
button.clicked.connect(click_OK)
next_question()
my_win.show()
app.exec_()