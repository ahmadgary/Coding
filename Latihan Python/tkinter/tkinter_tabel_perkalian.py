import tkinter as tk
from tkinter import messagebox

def show_multiplication_table():
    try:
        angka = int(entry.get())
        table = ""
        for i in range(1, 11):
            table += f"{angka} x {i} = {angka * i}\n"
        messagebox.showinfo("Tabel Perkalian", table)
    except ValueError as e:
        messagebox.showerror("Input Error", "Masukkan angka yang valid!")

# Create the main window
root = tk.Tk()
root.title("Tabel Perkalian")

# Create and place the widgets
tk.Label(root, text="Masukkan Angka:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Tampilkan Tabel", command=show_multiplication_table)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
