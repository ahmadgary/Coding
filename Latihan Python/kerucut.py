<<<<<<< HEAD:kerucut.py
print("Menghitung Luas dan Volume Kerucut")

r = float(input("Masukkan Jari-Jari: "))
t = float(input("Masukkan Tinggi: "))
luas_alas = float(input("Masukkan Luas Alas: "))
luas_selimut = float(input("Masukkan Luas Selimut: "))

phi = 22/7

volume = 1/3*(phi*r*r*t)
luas = luas_alas + luas_selimut
print("\nLuasnya \t\t:",luas)
=======
print("Menghitung Luas dan Volume Kerucut")

r = float(input("Masukkan Jari-Jari: "))
t = float(input("Masukkan Tinggi: "))
luas_alas = float(input("Masukkan Luas Alas: "))
luas_selimut = float(input("Masukkan Luas Selimut: "))

phi = 22/7

volume = 1/3*(phi*r*r*t)
luas = luas_alas + luas_selimut
print("\nLuasnya \t\t:",luas)
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/kerucut.py
print("\nVolumenya \t\t:",volume)