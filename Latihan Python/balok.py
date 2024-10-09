print("Menghitung Luas & Volume Balok")

panjang = float(input("\nMasukkan Panjang: "))
lebar = float(input("Masukkan Lebar: "))
tinggi = float(input("Masukkan Tinggi: "))

luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
volume = panjang*lebar*tinggi
print("\nLuas Balok \t\t:",luas)
print("\nVolume Balok \t\t:",volume)