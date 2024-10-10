import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class FactorialApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label1 = Label(text="Masukkan nilai:")
        self.input1 = TextInput(multiline=False)
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.input1)

        self.button = Button(text="Hitung Faktorial")
        self.button.bind(on_press=self.calculate)
        self.layout.add_widget(self.button)

        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate(self, instance):
        try:
            n = int(self.input1.text)
            faktorial = 1
            for i in range(1, n + 1):
                faktorial *= i
            self.result_label.text = f'{n}! = {faktorial}'
        except ValueError:
            self.result_label.text = "Masukkan angka yang valid."

if __name__ == "__main__":
    FactorialApp().run()