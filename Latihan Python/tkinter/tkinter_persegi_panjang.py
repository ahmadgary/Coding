import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())

        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)

        messagebox.showinfo("Hasil", f"Luas Persegi Panjang: {luas}\nKeliling Persegi Panjang: {keliling}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai numerik yang valid!")

# Setup Tkinter window
root = tk.Tk()
root.title("Kalkulator Persegi Panjang")

# Create and place labels and entries
tk.Label(root, text="Panjang (cm):").grid(row=0, column=0)
entry_panjang = tk.Entry(root)
entry_panjang.grid(row=0, column=1)

tk.Label(root, text="Lebar (cm):").grid(row=1, column=0)
entry_lebar = tk.Entry(root)
entry_lebar.grid(row=1, column=1)

# Create and place calculate button
tk.Button(root, text="Hitung", command=calculate).grid(row=2, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
