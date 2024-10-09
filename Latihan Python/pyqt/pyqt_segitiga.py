<<<<<<< HEAD:pyqt/pyqt_segitiga.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class TriangleCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menghitung Luas & Keliling Segitiga')

        self.alas_label = QLabel('Masukkan Alas:')
        self.alas_input = QLineEdit(self)

        self.tinggi_label = QLabel('Masukkan Tinggi:')
        self.tinggi_input = QLineEdit(self)

        self.calculate_button = QPushButton('Hitung', self)
        self.calculate_button.clicked.connect(self.calculate)

        self.luas_label = QLabel('Luasnya:')
        self.keliling_label = QLabel('Kelilingnya:')

        layout = QVBoxLayout()
        layout.addWidget(self.alas_label)
        layout.addWidget(self.alas_input)
        layout.addWidget(self.tinggi_label)
        layout.addWidget(self.tinggi_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.luas_label)
        layout.addWidget(self.keliling_label)

        self.setLayout(layout)

    def calculate(self):
        alas = float(self.alas_input.text())
        tinggi = float(self.tinggi_input.text())

        luas = 0.5 * alas * tinggi
        keliling = 3 * alas

        self.luas_label.setText(f'Luasnya: {luas}')
        self.keliling_label.setText(f'Kelilingnya: {keliling}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TriangleCalculator()
    ex.show()
    sys.exit(app.exec_())
=======
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class TriangleCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menghitung Luas & Keliling Segitiga')

        self.alas_label = QLabel('Masukkan Alas:')
        self.alas_input = QLineEdit(self)

        self.tinggi_label = QLabel('Masukkan Tinggi:')
        self.tinggi_input = QLineEdit(self)

        self.calculate_button = QPushButton('Hitung', self)
        self.calculate_button.clicked.connect(self.calculate)

        self.luas_label = QLabel('Luasnya:')
        self.keliling_label = QLabel('Kelilingnya:')

        layout = QVBoxLayout()
        layout.addWidget(self.alas_label)
        layout.addWidget(self.alas_input)
        layout.addWidget(self.tinggi_label)
        layout.addWidget(self.tinggi_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.luas_label)
        layout.addWidget(self.keliling_label)

        self.setLayout(layout)

    def calculate(self):
        alas = float(self.alas_input.text())
        tinggi = float(self.tinggi_input.text())

        luas = 0.5 * alas * tinggi
        keliling = 3 * alas

        self.luas_label.setText(f'Luasnya: {luas}')
        self.keliling_label.setText(f'Kelilingnya: {keliling}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TriangleCalculator()
    ex.show()
    sys.exit(app.exec_())
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/pyqt/pyqt_segitiga.py
