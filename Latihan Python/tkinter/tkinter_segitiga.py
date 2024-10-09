import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())

        luas = 0.5 * alas * tinggi
        keliling = 3 * alas  # Assuming an equilateral triangle

        messagebox.showinfo("Hasil", f"Luas Segitiga: {luas}\nKeliling Segitiga: {keliling}")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid.")

# Create the main window
root = tk.Tk()
root.title("Menghitung Luas & Keliling Segitiga")

# Create and place the input fields and labels
tk.Label(root, text="Masukkan Alas:").grid(row=0, column=0, padx=10, pady=5)
entry_alas = tk.Entry(root)
entry_alas.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Masukkan Tinggi:").grid(row=1, column=0, padx=10, pady=5)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=1, column=1, padx=10, pady=5)

# Create and place the calculate button
tk.Button(root, text="Hitung", command=calculate).grid(row=2, columnspan=2, pady=10)

# Run the application
root.mainloop()
