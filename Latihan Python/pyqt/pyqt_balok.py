<<<<<<< HEAD:pyqt/pyqt_balok.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class BalokCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menghitung Luas & Volume Balok')

        self.panjang_label = QLabel('Masukkan Panjang:')
        self.panjang_input = QLineEdit(self)

        self.lebar_label = QLabel('Masukkan Lebar:')
        self.lebar_input = QLineEdit(self)

        self.tinggi_label = QLabel('Masukkan Tinggi:')
        self.tinggi_input = QLineEdit(self)

        self.hitung_button = QPushButton('Hitung', self)
        self.hitung_button.clicked.connect(self.calculate)

        self.luas_label = QLabel('Luas Balok:')
        self.volume_label = QLabel('Volume Balok:')

        layout = QVBoxLayout()
        layout.addWidget(self.panjang_label)
        layout.addWidget(self.panjang_input)
        layout.addWidget(self.lebar_label)
        layout.addWidget(self.lebar_input)
        layout.addWidget(self.tinggi_label)
        layout.addWidget(self.tinggi_input)
        layout.addWidget(self.hitung_button)
        layout.addWidget(self.luas_label)
        layout.addWidget(self.volume_label)

        self.setLayout(layout)

    def calculate(self):
        panjang = float(self.panjang_input.text())
        lebar = float(self.lebar_input.text())
        tinggi = float(self.tinggi_input.text())

        luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
        volume = panjang * lebar * tinggi

        self.luas_label.setText(f'Luas Balok: {luas}')
        self.volume_label.setText(f'Volume Balok: {volume}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BalokCalculator()
    ex.show()
    sys.exit(app.exec_())
=======
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class BalokCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menghitung Luas & Volume Balok')

        self.panjang_label = QLabel('Masukkan Panjang:')
        self.panjang_input = QLineEdit(self)

        self.lebar_label = QLabel('Masukkan Lebar:')
        self.lebar_input = QLineEdit(self)

        self.tinggi_label = QLabel('Masukkan Tinggi:')
        self.tinggi_input = QLineEdit(self)

        self.hitung_button = QPushButton('Hitung', self)
        self.hitung_button.clicked.connect(self.calculate)

        self.luas_label = QLabel('Luas Balok:')
        self.volume_label = QLabel('Volume Balok:')

        layout = QVBoxLayout()
        layout.addWidget(self.panjang_label)
        layout.addWidget(self.panjang_input)
        layout.addWidget(self.lebar_label)
        layout.addWidget(self.lebar_input)
        layout.addWidget(self.tinggi_label)
        layout.addWidget(self.tinggi_input)
        layout.addWidget(self.hitung_button)
        layout.addWidget(self.luas_label)
        layout.addWidget(self.volume_label)

        self.setLayout(layout)

    def calculate(self):
        panjang = float(self.panjang_input.text())
        lebar = float(self.lebar_input.text())
        tinggi = float(self.tinggi_input.text())

        luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
        volume = panjang * lebar * tinggi

        self.luas_label.setText(f'Luas Balok: {luas}')
        self.volume_label.setText(f'Volume Balok: {volume}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BalokCalculator()
    ex.show()
    sys.exit(app.exec_())
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/pyqt/pyqt_balok.py
