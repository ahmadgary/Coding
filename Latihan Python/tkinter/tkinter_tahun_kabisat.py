import tkinter as tk
from tkinter import messagebox

def check_leap_year():
    try:
        tahun = int(entry_tahun.get())
        
        if (tahun % 4) == 0:
            if (tahun % 100) == 0:
                if (tahun % 400) == 0:
                    result = f"{tahun} adalah Tahun Kabisat"
                else:
                    result = f"{tahun} bukan Tahun Kabisat"
            else:
                result = f"{tahun} adalah Tahun Kabisat"
        else:
            result = f"{tahun} bukan Tahun Kabisat"
        
        messagebox.showinfo("Hasil", result)
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid")

# Setup Tkinter window
root = tk.Tk()
root.title("Pengecek Tahun Kabisat")

# Create and place labels and entries
tk.Label(root, text="Tulis Sebuah Tahun:").grid(row=0, column=0)
entry_tahun = tk.Entry(root)
entry_tahun.grid(row=0, column=1)

# Create and place check button
tk.Button(root, text="Cek", command=check_leap_year).grid(row=1, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
