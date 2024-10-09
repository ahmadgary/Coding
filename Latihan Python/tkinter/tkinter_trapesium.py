<<<<<<< HEAD:tkinter/tkinter_trapesium.py
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        sisi_alas = float(entry_sisi_alas.get())
        sisi_atas = float(entry_sisi_atas.get())
        tinggi = float(entry_tinggi.get())
        garis_miring1 = float(entry_garis_miring1.get())

        luas = 1/2 * (sisi_alas + sisi_atas) * tinggi
        keliling = sisi_alas + sisi_atas + 2 * garis_miring1

        messagebox.showinfo("Hasil", f"Luas Trapesium: {luas}\nKeliling Trapesium: {keliling}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai numerik yang valid!")

# Setup Tkinter window
root = tk.Tk()
root.title("Kalkulator Trapesium")

# Create and place labels and entries
tk.Label(root, text="Sisi Alas (cm):").grid(row=0, column=0)
entry_sisi_alas = tk.Entry(root)
entry_sisi_alas.grid(row=0, column=1)

tk.Label(root, text="Sisi Atas (cm):").grid(row=1, column=0)
entry_sisi_atas = tk.Entry(root)
entry_sisi_atas.grid(row=1, column=1)

tk.Label(root, text="Tinggi (cm):").grid(row=2, column=0)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=2, column=1)

tk.Label(root, text="Garis Miring Pertama (cm):").grid(row=3, column=0)
entry_garis_miring1 = tk.Entry(root)
entry_garis_miring1.grid(row=3, column=1)

# Create and place calculate button
tk.Button(root, text="Hitung", command=calculate).grid(row=4, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
=======
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        sisi_alas = float(entry_sisi_alas.get())
        sisi_atas = float(entry_sisi_atas.get())
        tinggi = float(entry_tinggi.get())
        garis_miring1 = float(entry_garis_miring1.get())

        luas = 1/2 * (sisi_alas + sisi_atas) * tinggi
        keliling = sisi_alas + sisi_atas + 2 * garis_miring1

        messagebox.showinfo("Hasil", f"Luas Trapesium: {luas}\nKeliling Trapesium: {keliling}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai numerik yang valid!")

# Setup Tkinter window
root = tk.Tk()
root.title("Kalkulator Trapesium")

# Create and place labels and entries
tk.Label(root, text="Sisi Alas (cm):").grid(row=0, column=0)
entry_sisi_alas = tk.Entry(root)
entry_sisi_alas.grid(row=0, column=1)

tk.Label(root, text="Sisi Atas (cm):").grid(row=1, column=0)
entry_sisi_atas = tk.Entry(root)
entry_sisi_atas.grid(row=1, column=1)

tk.Label(root, text="Tinggi (cm):").grid(row=2, column=0)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=2, column=1)

tk.Label(root, text="Garis Miring Pertama (cm):").grid(row=3, column=0)
entry_garis_miring1 = tk.Entry(root)
entry_garis_miring1.grid(row=3, column=1)

# Create and place calculate button
tk.Button(root, text="Hitung", command=calculate).grid(row=4, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/tkinter/tkinter_trapesium.py
