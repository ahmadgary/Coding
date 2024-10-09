<<<<<<< HEAD:pyside/pyside_bilangan_prima.py
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PrimeChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Prime Number Checker')
        self.layout = QVBoxLayout()

        self.label = QLabel('Masukkan Angka:')
        self.layout.addWidget(self.label)

        self.input = QLineEdit(self)
        self.layout.addWidget(self.input)

        self.button = QPushButton('Check', self)
        self.button.clicked.connect(self.check_prime)
        self.layout.addWidget(self.button)

        self.result = QLabel('')
        self.layout.addWidget(self.result)

        self.setLayout(self.layout)

    def check_prime(self):
        try:
            angka = int(self.input.text())
            prima = "adalah bilangan prima"

            if angka == 1 or angka == 0:
                prima = "bukan bilangan prima"
            for i in range(2, angka):
                if angka % i == 0:
                    prima = "bukan bilangan prima"
                    break

            self.result.setText(f'{angka} {prima}')
        except ValueError:
            self.result.setText('Masukkan angka yang valid!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checker = PrimeChecker()
    checker.show()
    sys.exit(app.exec())
=======
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PrimeChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Prime Number Checker')
        self.layout = QVBoxLayout()

        self.label = QLabel('Masukkan Angka:')
        self.layout.addWidget(self.label)

        self.input = QLineEdit(self)
        self.layout.addWidget(self.input)

        self.button = QPushButton('Check', self)
        self.button.clicked.connect(self.check_prime)
        self.layout.addWidget(self.button)

        self.result = QLabel('')
        self.layout.addWidget(self.result)

        self.setLayout(self.layout)

    def check_prime(self):
        try:
            angka = int(self.input.text())
            prima = "adalah bilangan prima"

            if angka == 1 or angka == 0:
                prima = "bukan bilangan prima"
            for i in range(2, angka):
                if angka % i == 0:
                    prima = "bukan bilangan prima"
                    break

            self.result.setText(f'{angka} {prima}')
        except ValueError:
            self.result.setText('Masukkan angka yang valid!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checker = PrimeChecker()
    checker.show()
    sys.exit(app.exec())
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/pyside/pyside_bilangan_prima.py
