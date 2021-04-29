import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Derick')  # alterando o nome da janela
        self.setFixedSize(400, 400)  # fixando o tamanho da janela
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)  # Para que a janela não receba texto (input)
        # alterando a cor da janela que mostra o resultado
        self.display.setStyleSheet('* {background: white; color: #000; font-size: 30px;}')
        # o botão se ajusta ao tamanho da janela e demais botões
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Adicionando o botão "7" na linha 1, coluna 0, ocupando 1 e 1 (lin, col)
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('*'), 1, 3, 1, 1)
        # limpa o display da calculadora
        self.add_btn(QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(''),
                     'background: #d5580d;')

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('/'), 2, 3, 1, 1)
        # apaga apenas o último caracter digitado
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(self.display.text()[:-1])
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('-'), 3, 3, 1, 1)
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('+'), 4, 3, 1, 1)
        self.add_btn(QPushButton('='), 4, 4, 1, 1, self.eval_igual)

        self.setCentralWidget(self.cw)

    # criando um método para adicionar botão, com linha, coluna
    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(lambda: self.display.setText((self.display.text() + btn.text())))
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        # o botão se ajusta ao tamanho da janela e demais botões
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText('Conta inválida.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
