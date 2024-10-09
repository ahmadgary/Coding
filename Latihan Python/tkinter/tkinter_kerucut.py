import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        r = float(entry_r.get())
        t = float(entry_t.get())
        luas_alas = float(entry_luas_alas.get())
        luas_selimut = float(entry_luas_selimut.get())
        
        phi = 22/7
        volume = 1/3 * (phi * r * r * t)
        luas = luas_alas + luas_selimut
        
        messagebox.showinfo("Hasil", f"Luasnya: {luas}\nVolumenya: {volume}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid")

# Setup Tkinter window
root = tk.Tk()
root.title("Menghitung Luas dan Volume Kerucut")

# Create and place labels and entries
tk.Label(root, text="Masukkan Jari-Jari:").grid(row=0, column=0)
entry_r = tk.Entry(root)
entry_r.grid(row=0, column=1)

tk.Label(root, text="Masukkan Tinggi:").grid(row=1, column=0)
entry_t = tk.Entry(root)
entry_t.grid(row=1, column=1)

tk.Label(root, text="Masukkan Luas Alas:").grid(row=2, column=0)
entry_luas_alas = tk.Entry(root)
entry_luas_alas.grid(row=2, column=1)

tk.Label(root, text="Masukkan Luas Selimut:").grid(row=3, column=0)
entry_luas_selimut = tk.Entry(root)
entry_luas_selimut.grid(row=3, column=1)

# Create and place calculate button
tk.Button(root, text="Hitung", command=calculate).grid(row=4, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
