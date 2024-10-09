<<<<<<< HEAD:tahun_hijriah.py
# Pastikan Anda telah menginstal pustaka hijridate
# Anda dapat menginstalnya dengan menjalankan: pip install hijridate

from hijridate import Gregorian

# Fungsi untuk mengkonversi tahun Masehi ke tahun Hijriah
def masehi_ke_hijriah(tahun, bulan, hari):
    hijri_date = Gregorian(tahun, bulan, hari).to_hijri()
    return hijri_date

# Input tahun, bulan, dan hari Masehi dari pengguna
tahun = int(input("Tulis Sebuah Tahun: "))
bulan = int(input("Tulis Sebuah Bulan: "))
hari = int(input("Tulis Sebuah Hari: "))

# Konversi ke tanggal Hijriah
tanggal_hijriah = masehi_ke_hijriah(tahun, bulan, hari)
print(f"Tanggal Hijriah: {tanggal_hijriah}")
=======
# Pastikan Anda telah menginstal pustaka hijridate
# Anda dapat menginstalnya dengan menjalankan: pip install hijridate

from hijridate import Gregorian

# Fungsi untuk mengkonversi tahun Masehi ke tahun Hijriah
def masehi_ke_hijriah(tahun, bulan, hari):
    hijri_date = Gregorian(tahun, bulan, hari).to_hijri()
    return hijri_date

# Input tahun, bulan, dan hari Masehi dari pengguna
tahun = int(input("Tulis Sebuah Tahun: "))
bulan = int(input("Tulis Sebuah Bulan: "))
hari = int(input("Tulis Sebuah Hari: "))

# Konversi ke tanggal Hijriah
tanggal_hijriah = masehi_ke_hijriah(tahun, bulan, hari)
print(f"Tanggal Hijriah: {tanggal_hijriah}")
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/tahun_hijriah.py
