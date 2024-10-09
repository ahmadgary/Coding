import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LeapYearApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label1 = Label(text="Tulis Sebuah Tahun:")
        self.input1 = TextInput(multiline=False)
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.input1)

        self.button = Button(text="Cek Tahun Kabisat")
        self.button.bind(on_press=self.calculate)
        self.layout.add_widget(self.button)

        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate(self, instance):
        try:
            tahun = int(self.input1.text)
            if (tahun % 4) == 0:
                if (tahun % 100) == 0:
                    if (tahun % 400) == 0:
                        self.result_label.text = f"{tahun} adalah Tahun Kabisat"
                    else:
                        self.result_label.text = f"{tahun} bukan Tahun Kabisat"
                else:
                    self.result_label.text = f"{tahun} adalah Tahun Kabisat"
            else:
                self.result_label.text = f"{tahun} bukan Tahun Kabisat"
        except ValueError:
            self.result_label.text = "Masukkan angka yang valid."

if __name__ == "__main__":
    LeapYearApp().run()