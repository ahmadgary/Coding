<<<<<<< HEAD:tkinter/tkinter_tabel_pertambahan.py
import tkinter as tk
from tkinter import messagebox

def show_addition_table():
    try:
        angka = int(entry.get())
        table = ""
        for i in range(1, 11):
            table += f"{angka} + {i} = {angka + i}\n"
        messagebox.showinfo("Tabel Pertambahan", table)
    except ValueError as e:
        messagebox.showerror("Input Error", "Masukkan angka yang valid!")

# Create the main window
root = tk.Tk()
root.title("Tabel Pertambahan")

# Create and place the widgets
tk.Label(root, text="Masukkan Angka:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Tampilkan Tabel", command=show_addition_table)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
=======
import tkinter as tk
from tkinter import messagebox

def show_addition_table():
    try:
        angka = int(entry.get())
        table = ""
        for i in range(1, 11):
            table += f"{angka} + {i} = {angka + i}\n"
        messagebox.showinfo("Tabel Pertambahan", table)
    except ValueError as e:
        messagebox.showerror("Input Error", "Masukkan angka yang valid!")

# Create the main window
root = tk.Tk()
root.title("Tabel Pertambahan")

# Create and place the widgets
tk.Label(root, text="Masukkan Angka:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Tampilkan Tabel", command=show_addition_table)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/tkinter/tkinter_tabel_pertambahan.py
