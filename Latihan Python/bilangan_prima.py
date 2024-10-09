angka = int(input("Masukkan Angka :"))
prima = "adalah bilangan prima"

if (angka == 1 or angka == 0):
    prima = "bukan bilangan prima"
for i in range (2, angka):
    if (angka % i == 0):
        prima = "bukan bilangan prima"
print (angka, prima)