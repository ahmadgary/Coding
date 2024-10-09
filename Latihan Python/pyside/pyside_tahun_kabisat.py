import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class LeapYearChecker(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Leap Year Checker')

        self.layout = QVBoxLayout()

        self.label = QLabel('Tulis Sebuah Tahun:')
        self.layout.addWidget(self.label)

        self.year_input = QLineEdit()
        self.layout.addWidget(self.year_input)

        self.check_button = QPushButton('Check')
        self.check_button.clicked.connect(self.check_leap_year)
        self.layout.addWidget(self.check_button)

        self.result_label = QLabel('')
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def check_leap_year(self):
        try:
            tahun = int(self.year_input.text())
            if (tahun % 4) == 0:
                if (tahun % 100) == 0:
                    if (tahun % 400) == 0:
                        self.result_label.setText(f"{tahun} adalah Tahun Kabisat")
                    else:
                        self.result_label.setText(f"{tahun} bukan Tahun Kabisat")
                else:
                    self.result_label.setText(f"{tahun} adalah Tahun Kabisat")
            else:
                self.result_label.setText(f"{tahun} bukan Tahun Kabisat")
        except ValueError:
            self.result_label.setText("Masukkan tahun yang valid")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LeapYearChecker()
    ex.show()
    sys.exit(app.exec())
