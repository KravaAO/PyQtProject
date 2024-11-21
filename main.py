from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('Тест Руфʼє')
window.resize(400, 200)

def start():
    global second_win, text_input1
    window.hide()
    second_win = QWidget()
    second_win.setWindowTitle('Тестування для '+text_input1.text().title())
    second_win.resize(400, 200)
    v_line = QVBoxLayout()
    inst_text = QLabel('Тут можно прописати інструкцію')

    text_input1 = QLineEdit()
    text_input1.setPlaceholderText('Введіть пульс до присідань')

    btn = QPushButton('Розпочати тестування')

    v_line.addWidget(inst_text)
    v_line.addWidget(text_input1)
    v_line.addWidget(btn)
    second_win.setLayout(v_line)
    second_win.show()

# створення шаблону
v_line = QVBoxLayout()

# стоврення віджетів
inst_text = QLabel('Інструкція додатка ...')
text_input1 = QLineEdit() # це та лінія на якій можно писати
text_input1.setPlaceholderText('Введіть імʼя') # додавання до ліннії підсказки з питанням
btn = QPushButton('Розпочати тестування')

# додавання віджетів до шаблону
v_line.addWidget(inst_text)
v_line.addWidget(text_input1)
v_line.addWidget(btn)

# додавання шаблону до вікна
window.setLayout(v_line)

# підключення функціїї на клік по кнопці
btn.clicked.connect(start)

# запуск основного вікна та цикла подій додатка
window.show()
app.exec_()