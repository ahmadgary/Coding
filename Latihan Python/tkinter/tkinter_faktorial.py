import tkinter as tk
from tkinter import messagebox

def calculate_factorial():
    try:
        n = int(entry.get())
        if n < 0:
            raise ValueError("Nilai harus non-negatif")
        faktorial = 1
        for i in range(1, n + 1):
            faktorial *= i
        messagebox.showinfo("Hasil", f'{n}! = {faktorial}')
    except ValueError as e:
        messagebox.showerror("Input Error", "Masukkan nilai yang valid")

# Create the main window
root = tk.Tk()
root.title("Faktorial Calculator")

# Create and place the widgets
tk.Label(root, text="Masukkan nilai:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Hitung Faktorial", command=calculate_factorial)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
