sisi_alas = float(input("Masukkan sisi alas trapesium (cm): "))
sisi_atas = float(input("Masukkan sisi atas trapesium (cm): "))
tinggi = float(input("Masukkan tinggi trapesium (cm): "))
garis_miring1 = float(input("Masukkan garis miring pertama (cm): "))

luas = 1/2*(sisi_alas + sisi_atas)*tinggi
print("\nLuas Trapesium \t\t:",luas)

keliling = sisi_alas + sisi_atas + garis_miring1 + garis_miring1
print("\nKeliling Trapesium \t\t:",keliling)