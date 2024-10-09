import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from hijridate import Gregorian

class HijriConverterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label1 = Label(text="Tulis Sebuah Tahun:")
        self.input1 = TextInput(multiline=False)
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.input1)

        self.label2 = Label(text="Tulis Sebuah Bulan:")
        self.input2 = TextInput(multiline=False)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.input2)

        self.label3 = Label(text="Tulis Sebuah Hari:")
        self.input3 = TextInput(multiline=False)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.input3)

        self.button = Button(text="Konversi ke Hijriah")
        self.button.bind(on_press=self.calculate)
        self.layout.add_widget(self.button)

        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate(self, instance):
        try:
            tahun = int(self.input1.text)
            bulan = int(self.input2.text)
            hari = int(self.input3.text)
            tanggal_hijriah = Gregorian(tahun, bulan, hari).to_hijri()
            self.result_label.text = f"Tanggal Hijriah: {tanggal_hijriah}"
        except ValueError:
            self.result_label.text = "Masukkan angka yang valid."

if __name__ == "__main__":
    HijriConverterApp().run()
