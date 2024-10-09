import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BalokApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label1 = Label(text="Masukkan Panjang:")
        self.input1 = TextInput(multiline=False)
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.input1)

        self.label2 = Label(text="Masukkan Lebar:")
        self.input2 = TextInput(multiline=False)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.input2)

        self.label3 = Label(text="Masukkan Tinggi:")
        self.input3 = TextInput(multiline=False)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.input3)

        self.button = Button(text="Hitung")
        self.button.bind(on_press=self.calculate)
        self.layout.add_widget(self.button)

        self.result_label1 = Label(text="Luas Balok: ")
        self.result_label2 = Label(text="Volume Balok: ")
        self.layout.add_widget(self.result_label1)
        self.layout.add_widget(self.result_label2)

        return self.layout

    def calculate(self, instance):
        panjang = float(self.input1.text)
        lebar = float(self.input2.text)
        tinggi = float(self.input3.text)
        
        luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
        volume = panjang*lebar*tinggi

        self.result_label1.text = f"Luas Balok: {luas}"
        self.result_label2.text = f"Volume Balok: {volume}"

if __name__ == "__main__":
    BalokApp().run()
