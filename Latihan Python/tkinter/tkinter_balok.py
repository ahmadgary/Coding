import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())

        luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
        volume = panjang * lebar * tinggi

        messagebox.showinfo("Hasil", f"Luas Balok: {luas} \nVolume Balok: {volume} ")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid.")

# Create the main window
root = tk.Tk()
root.title("Menghitung Luas & Volume Balok")

# Create and place the input fields and labels
tk.Label(root, text="Masukkan Panjang:").grid(row=0, column=0, padx=10, pady=5)
entry_panjang = tk.Entry(root)
entry_panjang.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Masukkan Lebar:").grid(row=1, column=0, padx=10, pady=5)
entry_lebar = tk.Entry(root)
entry_lebar.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Masukkan Tinggi:").grid(row=2, column=0, padx=10, pady=5)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=2, column=1, padx=10, pady=5)

# Create and place the calculate button
tk.Button(root, text="Hitung", command=calculate).grid(row=3, columnspan=2, pady=10)
# Run the application
root.mainloop()
