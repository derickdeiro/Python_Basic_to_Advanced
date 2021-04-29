"""
PyQT é um tookit desenvolvido em C++ utilizado por vários programas para criação de
aplicações GUI (Interface Gráfica). Também inclui diversas funcionalidades, como: acesso
a base de dados, threads, comunicação de rede, etc...
pip install pyqt5
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do Botão')
        # semelhante ao CSS
        self.btn.setStyleSheet('font-size: 40px;')
        # grid é grade com linhas e coluna. Linha 0, coluna 0.
        # Quantas linhas e colunas o botão vai ocupar.
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        # pegando o evento de quando o botão é clicado.
        self.btn.clicked.connect(lambda: print('Olá mundo!'))  # isso é uma função anônima
        self.btn.clicked.connect(self.acao)  # isso é um método dedicado

        self.setCentralWidget(self.cw)

    def acao(self):
        print('Alguma coisa...')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
