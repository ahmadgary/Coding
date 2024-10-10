import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Faktorial Calculator", size=(300, 200))
        panel = wx.Panel(self)

        self.label = wx.StaticText(panel, label="Masukkan nilai:", pos=(10, 10))
        self.input = wx.TextCtrl(panel, pos=(120, 10), size=(150, -1))

        self.button = wx.Button(panel, label="Hitung Faktorial", pos=(10, 50))
        self.button.Bind(wx.EVT_BUTTON, self.calculate_factorial)

        self.result_label = wx.StaticText(panel, label="", pos=(10, 100))

    def calculate_factorial(self, event):
        try:
            n = int(self.input.GetValue())
            faktorial = 1
            for i in range(1, n + 1):
                faktorial *= i
            self.result_label.SetLabel(f'{n}! = {faktorial}')
        except ValueError:
            self.result_label.SetLabel("Masukkan angka yang valid.")

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
