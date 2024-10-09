import tkinter as tk
from tkinter import messagebox

def check_prime():
    try:
        angka = int(entry_angka.get())
        prima = "adalah bilangan prima"
        
        if angka == 1 or angka == 0:
            prima = "bukan bilangan prima"
        for i in range(2, angka):
            if angka % i == 0:
                prima = "bukan bilangan prima"
                break
        
        messagebox.showinfo("Hasil", f"{angka} {prima}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid")

# Setup Tkinter window
root = tk.Tk()
root.title("Pengecek Bilangan Prima")

# Create and place labels and entries
tk.Label(root, text="Masukkan Angka:").grid(row=0, column=0)
entry_angka = tk.Entry(root)
entry_angka.grid(row=0, column=1)

# Create and place check button
tk.Button(root, text="Cek", command=check_prime).grid(row=1, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
