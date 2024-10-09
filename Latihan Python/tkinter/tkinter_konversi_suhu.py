import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        choice = int(entry_choice.get())

        if choice == 1:
            result = (temperature * 9/5) + 32
            messagebox.showinfo("Hasil Konversi", f"{temperature} Celsius = {result} Fahrenheit")
        elif choice == 2:
            result = temperature * 4/5
            messagebox.showinfo("Hasil Konversi", f"{temperature} Celsius = {result} Reamur")
        elif choice == 3:
            result = temperature + 273.15
            messagebox.showinfo("Hasil Konversi", f"{temperature} Celsius = {result} Kelvin")
        elif choice == 4:
            result = (temperature + 273.15) * 9/5
            messagebox.showinfo("Hasil Konversi", f"{temperature} Celsius = {result} Rankine")
        elif choice == 5:
            result = (temperature - 32) * 5/9
            messagebox.showinfo("Hasil Konversi", f"{temperature} Fahrenheit = {result} Celsius")
        elif choice == 6:
            result = (temperature - 32) * 4/9
            messagebox.showinfo("Hasil Konversi", f"{temperature} Fahrenheit = {result} Reamur")
        elif choice == 7:
            result = (temperature + 459.67) * 5/9
            messagebox.showinfo("Hasil Konversi", f"{temperature} Fahrenheit = {result} Kelvin")
        elif choice == 8:
            result = temperature + 459.67
            messagebox.showinfo("Hasil Konversi", f"{temperature} Fahrenheit = {result} Rankine")
        elif choice == 9:
            result = temperature * 5/4
            messagebox.showinfo("Hasil Konversi", f"{temperature} Reamur = {result} Celsius")
        elif choice == 10:
            result = (temperature * 9/4) + 32
            messagebox.showinfo("Hasil Konversi", f"{temperature} Reamur = {result} Fahrenheit")
        elif choice == 11:
            result = (temperature * 5/4) + 273.15
            messagebox.showinfo("Hasil Konversi", f"{temperature} Reamur = {result} Kelvin")
        elif choice == 12:
            result = (temperature * 9/4) + 491.67
            messagebox.showinfo("Hasil Konversi", f"{temperature} Reamur = {result} Rankine")
        elif choice == 13:
            result = temperature - 273.15
            messagebox.showinfo("Hasil Konversi", f"{temperature} Kelvin = {result} Celsius")
        elif choice == 14:
            result = (temperature * 9/5) - 459.67
            messagebox.showinfo("Hasil Konversi", f"{temperature} Kelvin = {result} Fahrenheit")
        elif choice == 15:
            result = (temperature - 273.15) * 4/5
            messagebox.showinfo("Hasil Konversi", f"{temperature} Kelvin = {result} Reamur")
        elif choice == 16:
            result = temperature * 9/5
            messagebox.showinfo("Hasil Konversi", f"{temperature} Kelvin = {result} Rankine")
        elif choice == 17:
            result = (temperature - 491.67) * 5/9
            messagebox.showinfo("Hasil Konversi", f"{temperature} Rankine = {result} Celsius")
        elif choice == 18:
            result = temperature - 459.67
            messagebox.showinfo("Hasil Konversi", f"{temperature} Rankine = {result} Fahrenheit")
        elif choice == 19:
            result = (temperature - 491.67) * 4/9
            messagebox.showinfo("Hasil Konversi", f"{temperature} Rankine = {result} Reamur")
        elif choice == 20:
            result = temperature * 5/9
            messagebox.showinfo("Hasil Konversi", f"{temperature} Rankine = {result} Kelvin")
        else:
            messagebox.showerror("Input Error", "Pilihan tidak valid. Masukkan angka antara 1 dan 20.")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid.")

# Create the main window
root = tk.Tk()
root.title("Konversi Suhu")

# Create and place the input fields and labels
tk.Label(root, text="Masukkan Pilihan (1-20):").grid(row=0, column=0, padx=10, pady=5)
entry_choice = tk.Entry(root)
entry_choice.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Masukkan Suhu:").grid(row=1, column=0, padx=10, pady=5)
entry_temperature = tk.Entry(root)
entry_temperature.grid(row=1, column=1, padx=10, pady=5)

# Create and place the convert button
tk.Button(root, text="Konversi", command=convert_temperature).grid(row=2, columnspan=2, pady=10)

# Run the application
root.mainloop()
