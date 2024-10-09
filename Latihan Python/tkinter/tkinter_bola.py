import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        r = float(entry.get())
        phi = 22/7
        volume = 4/3*(phi*r*r*r)
        luas = 4*phi*r*r
        messagebox.showinfo("Result", f"Luasnya: {luas}\nVolumenya: {volume}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Menghitung Luas & Volume Bola")

# Create and place the widgets
label = tk.Label(root, text="Masukkan Jari-Jari:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Hitung", command=calculate)
button.pack(pady=20)

# Run the application
root.mainloop()
