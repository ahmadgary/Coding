<<<<<<< HEAD:tkinter/tkinter_tahun_hijriah.py
# Pastikan Anda telah menginstal pustaka hijridate
# Anda dapat menginstalnya dengan menjalankan: pip install hijridate

import tkinter as tk
from tkinter import messagebox
from hijridate import Gregorian

# Fungsi untuk mengkonversi tahun Masehi ke tahun Hijriah
def masehi_ke_hijriah():
    try:
        tahun = int(entry_tahun.get())
        bulan = int(entry_bulan.get())
        hari = int(entry_hari.get())
        hijri_date = Gregorian(tahun, bulan, hari).to_hijri()
        messagebox.showinfo("Hasil Konversi", f"Tanggal Hijriah: {hijri_date}")
    except ValueError:
        messagebox.showerror("Kesalahan", "Masukkan nilai tahun, bulan, dan hari yang valid.")

# Membuat jendela utama
root = tk.Tk()
root.title("Konversi Tahun Masehi ke Hijriah")

# Membuat dan menempatkan label dan entri untuk input tahun, bulan, dan hari
label_tahun = tk.Label(root, text="Tulis Sebuah Tahun:")
label_tahun.pack()
entry_tahun = tk.Entry(root)
entry_tahun.pack()

label_bulan = tk.Label(root, text="Tulis Sebuah Bulan:")
label_bulan.pack()
entry_bulan = tk.Entry(root)
entry_bulan.pack()

label_hari = tk.Label(root, text="Tulis Sebuah Hari:")
label_hari.pack()
entry_hari = tk.Entry(root)
entry_hari.pack()

# Membuat dan menempatkan tombol untuk melakukan konversi
button_konversi = tk.Button(root, text="Konversi", command=masehi_ke_hijriah)
button_konversi.pack()

# Menjalankan aplikasi
root.mainloop()
=======
# Pastikan Anda telah menginstal pustaka hijridate
# Anda dapat menginstalnya dengan menjalankan: pip install hijridate

import tkinter as tk
from tkinter import messagebox
from hijridate import Gregorian

# Fungsi untuk mengkonversi tahun Masehi ke tahun Hijriah
def masehi_ke_hijriah():
    try:
        tahun = int(entry_tahun.get())
        bulan = int(entry_bulan.get())
        hari = int(entry_hari.get())
        hijri_date = Gregorian(tahun, bulan, hari).to_hijri()
        messagebox.showinfo("Hasil Konversi", f"Tanggal Hijriah: {hijri_date}")
    except ValueError:
        messagebox.showerror("Kesalahan", "Masukkan nilai tahun, bulan, dan hari yang valid.")

# Membuat jendela utama
root = tk.Tk()
root.title("Konversi Tahun Masehi ke Hijriah")

# Membuat dan menempatkan label dan entri untuk input tahun, bulan, dan hari
label_tahun = tk.Label(root, text="Tulis Sebuah Tahun:")
label_tahun.pack()
entry_tahun = tk.Entry(root)
entry_tahun.pack()

label_bulan = tk.Label(root, text="Tulis Sebuah Bulan:")
label_bulan.pack()
entry_bulan = tk.Entry(root)
entry_bulan.pack()

label_hari = tk.Label(root, text="Tulis Sebuah Hari:")
label_hari.pack()
entry_hari = tk.Entry(root)
entry_hari.pack()

# Membuat dan menempatkan tombol untuk melakukan konversi
button_konversi = tk.Button(root, text="Konversi", command=masehi_ke_hijriah)
button_konversi.pack()

# Menjalankan aplikasi
root.mainloop()
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/tkinter/tkinter_tahun_hijriah.py
