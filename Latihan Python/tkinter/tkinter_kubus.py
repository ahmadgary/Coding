<<<<<<< HEAD:tkinter/tkinter_kubus.py
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        r = float(entry_r.get())

        luas = 6 * r * r
        volume = r * r * r

        messagebox.showinfo("Hasil", f"Luas Kubus: {luas}\nVolume Kubus: {volume}")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid.")

# Create the main window
root = tk.Tk()
root.title("Menghitung Luas & Volume Kubus")

# Create and place the input fields and labels
tk.Label(root, text="Masukkan Rusuknya:").grid(row=0, column=0, padx=10, pady=5)
entry_r = tk.Entry(root)
entry_r.grid(row=0, column=1, padx=10, pady=5)

# Create and place the calculate button
tk.Button(root, text="Hitung", command=calculate).grid(row=1, columnspan=2, pady=10)

# Run the application
root.mainloop()
=======
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        r = float(entry_r.get())

        luas = 6 * r * r
        volume = r * r * r

        messagebox.showinfo("Hasil", f"Luas Kubus: {luas}\nVolume Kubus: {volume}")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid.")

# Create the main window
root = tk.Tk()
root.title("Menghitung Luas & Volume Kubus")

# Create and place the input fields and labels
tk.Label(root, text="Masukkan Rusuknya:").grid(row=0, column=0, padx=10, pady=5)
entry_r = tk.Entry(root)
entry_r.grid(row=0, column=1, padx=10, pady=5)

# Create and place the calculate button
tk.Button(root, text="Hitung", command=calculate).grid(row=1, columnspan=2, pady=10)

# Run the application
root.mainloop()
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/tkinter/tkinter_kubus.py
