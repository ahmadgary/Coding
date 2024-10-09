<<<<<<< HEAD:bilangan_prima.py
angka = int(input("Masukkan Angka :"))
prima = "adalah bilangan prima"

if (angka == 1 or angka == 0):
    prima = "bukan bilangan prima"
for i in range (2, angka):
    if (angka % i == 0):
        prima = "bukan bilangan prima"
=======
angka = int(input("Masukkan Angka :"))
prima = "adalah bilangan prima"

if (angka == 1 or angka == 0):
    prima = "bukan bilangan prima"
for i in range (2, angka):
    if (angka % i == 0):
        prima = "bukan bilangan prima"
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/bilangan_prima.py
print (angka, prima)