from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QPushButton

from main import window

v_line = QVBoxLayout()

text_input1 = QLineEdit()
text_input1.setPlaceholderText('Введіть імʼя')

btn = QPushButton('Розпочати тестування')

v_line.addWidget(text_input1)
v_line.addWidget(btn)

window.setLayout(v_line)