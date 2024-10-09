<<<<<<< HEAD:tkinter/tkinter_persegi.py
import tkinter as tk
from tkinter import messagebox

def calculate_square():
    try:
        s = float(entry.get())
        if s < 0:
            raise ValueError("Nilai harus non-negatif")
        luas = s * s
        keliling = 4 * s
        messagebox.showinfo("Hasil", f"Luasnya: {luas}\nKeliling: {keliling}")
    except ValueError as e:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid!")

# Create the main window
root = tk.Tk()
root.title("Kalkulator Persegi")

# Create and place the widgets
tk.Label(root, text="Masukkan Sisi:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Hitung", command=calculate_square)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
=======
import tkinter as tk
from tkinter import messagebox

def calculate_square():
    try:
        s = float(entry.get())
        if s < 0:
            raise ValueError("Nilai harus non-negatif")
        luas = s * s
        keliling = 4 * s
        messagebox.showinfo("Hasil", f"Luasnya: {luas}\nKeliling: {keliling}")
    except ValueError as e:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid!")

# Create the main window
root = tk.Tk()
root.title("Kalkulator Persegi")

# Create and place the widgets
tk.Label(root, text="Masukkan Sisi:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Hitung", command=calculate_square)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/tkinter/tkinter_persegi.py
