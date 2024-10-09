<<<<<<< HEAD:pyside/pyside_balok.py
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class BalokCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menghitung Luas & Volume Balok")
        
        layout = QVBoxLayout()

        self.panjang_label = QLabel("Masukkan Panjang:")
        self.panjang_input = QLineEdit()
        layout.addWidget(self.panjang_label)
        layout.addWidget(self.panjang_input)

        self.lebar_label = QLabel("Masukkan Lebar:")
        self.lebar_input = QLineEdit()
        layout.addWidget(self.lebar_label)
        layout.addWidget(self.lebar_input)

        self.tinggi_label = QLabel("Masukkan Tinggi:")
        self.tinggi_input = QLineEdit()
        layout.addWidget(self.tinggi_label)
        layout.addWidget(self.tinggi_input)

        self.calculate_button = QPushButton("Hitung")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.luas_label = QLabel("Luas Balok:")
        layout.addWidget(self.luas_label)

        self.volume_label = QLabel("Volume Balok:")
        layout.addWidget(self.volume_label)

        self.setLayout(layout)

    def calculate(self):
        panjang = float(self.panjang_input.text())
        lebar = float(self.lebar_input.text())
        tinggi = float(self.tinggi_input.text())

        luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
        volume = panjang * lebar * tinggi

        self.luas_label.setText(f"Luas Balok: {luas}")
        self.volume_label.setText(f"Volume Balok: {volume}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = BalokCalculator()
    calculator.show()
    sys.exit(app.exec())
=======
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class BalokCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menghitung Luas & Volume Balok")
        
        layout = QVBoxLayout()

        self.panjang_label = QLabel("Masukkan Panjang:")
        self.panjang_input = QLineEdit()
        layout.addWidget(self.panjang_label)
        layout.addWidget(self.panjang_input)

        self.lebar_label = QLabel("Masukkan Lebar:")
        self.lebar_input = QLineEdit()
        layout.addWidget(self.lebar_label)
        layout.addWidget(self.lebar_input)

        self.tinggi_label = QLabel("Masukkan Tinggi:")
        self.tinggi_input = QLineEdit()
        layout.addWidget(self.tinggi_label)
        layout.addWidget(self.tinggi_input)

        self.calculate_button = QPushButton("Hitung")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.luas_label = QLabel("Luas Balok:")
        layout.addWidget(self.luas_label)

        self.volume_label = QLabel("Volume Balok:")
        layout.addWidget(self.volume_label)

        self.setLayout(layout)

    def calculate(self):
        panjang = float(self.panjang_input.text())
        lebar = float(self.lebar_input.text())
        tinggi = float(self.tinggi_input.text())

        luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
        volume = panjang * lebar * tinggi

        self.luas_label.setText(f"Luas Balok: {luas}")
        self.volume_label.setText(f"Volume Balok: {volume}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = BalokCalculator()
    calculator.show()
    sys.exit(app.exec())
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/pyside/pyside_balok.py
