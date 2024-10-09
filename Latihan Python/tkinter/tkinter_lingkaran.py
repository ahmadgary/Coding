<<<<<<< HEAD:tkinter/tkinter_lingkaran.py
import tkinter as tk
from tkinter import messagebox

def calculate_circle():
    try:
        r = float(entry.get())
        if r < 0:
            raise ValueError("Nilai harus non-negatif")
        phi = 3.14
        diameter = 2 * r
        luas = phi * r * r
        keliling = phi * diameter
        messagebox.showinfo("Hasil", f"Luas: {luas:.2f}\nKeliling: {keliling:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid!")

# Create the main window
root = tk.Tk()
root.title("Kalkulator Lingkaran")

# Create and place the widgets
tk.Label(root, text="Masukkan Nilai Jari-Jari:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Hitung", command=calculate_circle)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
=======
import tkinter as tk
from tkinter import messagebox

def calculate_circle():
    try:
        r = float(entry.get())
        if r < 0:
            raise ValueError("Nilai harus non-negatif")
        phi = 3.14
        diameter = 2 * r
        luas = phi * r * r
        keliling = phi * diameter
        messagebox.showinfo("Hasil", f"Luas: {luas:.2f}\nKeliling: {keliling:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid!")

# Create the main window
root = tk.Tk()
root.title("Kalkulator Lingkaran")

# Create and place the widgets
tk.Label(root, text="Masukkan Nilai Jari-Jari:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Hitung", command=calculate_circle)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/tkinter/tkinter_lingkaran.py
