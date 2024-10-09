import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        choice = int(entry_choice.get())
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if choice == 1:
            result = num1 + num2
            messagebox.showinfo("Hasil", f"{num1} + {num2} = {result}")
        elif choice == 2:
            result = num1 - num2
            messagebox.showinfo("Hasil", f"{num1} - {num2} = {result}")
        elif choice == 3:
            result = num1 * num2
            messagebox.showinfo("Hasil", f"{num1} x {num2} = {result}")
        elif choice == 4:
            if num2 == 0:
                result = "0"
            else:
                result = num1 / num2
            messagebox.showinfo("Hasil", f"{num1} / {num2} = {result}")
        else:
            messagebox.showerror("Input Error", "Pilihan tidak valid. Masukkan angka antara 1 dan 4.")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid.")

# Create the main window
root = tk.Tk()
root.title("Kalkulator")

# Create and place the input fields and labels
tk.Label(root, text="Masukkan Pilihan (1/2/3/4):").grid(row=0, column=0, padx=10, pady=5)
entry_choice = tk.Entry(root)
entry_choice.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Masukkan Bilangan Pertama:").grid(row=1, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Masukkan Bilangan Kedua:").grid(row=2, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1, padx=10, pady=5)

# Create and place the calculate button
tk.Button(root, text="Hitung", command=calculate).grid(row=3, columnspan=2, pady=10)

# Run the application
root.mainloop()
