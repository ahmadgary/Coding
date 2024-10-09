import tkinter as tk
from tkinter import messagebox

def show_table():
    try:
        angka = int(entry.get())
        result = ""
        for i in range(1, 11):
            result += f"{angka} - {i} = {angka - i}\n"
        messagebox.showinfo("Tabel Pengurangan", result)
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid!")

root = tk.Tk()
root.title("Tabel Pengurangan")

tk.Label(root, text="Masukkan Angka:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Tampilkan Tabel", command=show_table).pack()

root.mainloop()
