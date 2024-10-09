<<<<<<< HEAD:konversi_suhu.py
print("Konveri Suhu")
print("1. Celsius ke Fahrenheit")
print("2. Celsius ke Reamur")
print("3. Celsius ke Kelvin")
print("4. Celsius ke Rankine")
print("5. Fahrenheit ke Celsius")
print("6. Fahrenheit ke Reamur")
print("7. Fahrenheit ke Kelvin")
print("8. Fahrenheit ke Rankine")
print("9. Reamur ke Celsius")
print("10. Reamur ke Fahrenheit")
print("11. Reamur ke Kelvin")
print("12. Reamur ke Rankine")
print("13. Kelvin ke Celsius")
print("14. Kelvin ke Fahrenheit")
print("15. Kelvin ke Reamur")
print("16. Kelvin ke Rankine")
print("17. Rankine ke Celsius")
print("18. Rankine ke Fahrenheit")
print("19. Rankine ke Reamur")
print("20. Rankine ke Kelvin")

p = int(input("Masukkan Pilihan (1-20): "))
temperature = float(input("Masukkan Suhu: "))

if p == 1:
    result = (temperature * 9/5) + 32
    print(temperature, "Celsius =", result, "Fahrenheit")
elif p == 2:
    result = temperature * 4/5
    print(temperature, "Celsius =", result, "Reamur")
elif p == 3:
    result = temperature + 273.15
    print(temperature, "Celsius =", result, "Kelvin")
elif p == 4:
    result = (temperature + 273.15) * 9/5
    print(temperature, "Celsius =", result, "Rankine")
elif p == 5:
    result = (temperature - 32) * 5/9
    print(temperature, "Fahrenheit =", result, "Celsius")
elif p == 6:
    result = (temperature - 32) * 4/9
    print(temperature, "Fahrenheit =", result, "Reamur")
elif p == 7:
    result = (temperature + 459.67) * 5/9
    print(temperature, "Fahrenheit =", result, "Kelvin")
elif p == 8:
    result = temperature + 459.67
    print(temperature, "Fahrenheit =", result, "Rankine")
elif p == 9:
    result = temperature * 5/4
    print(temperature, "Reamur =", result, "Celsius")
elif p == 10:
    result = (temperature * 9/4) + 32
    print(temperature, "Reamur =", result, "Fahrenheit")
elif p == 11:
    result = (temperature * 5/4) + 273.15
    print(temperature, "Reamur =", result, "Kelvin")
elif p == 12:
    result = (temperature * 9/4) + 491.67
    print(temperature, "Reamur =", result, "Rankine")
elif p == 13:
    result = temperature - 273.15
    print(temperature, "Kelvin =", result, "Celsius")
elif p == 14:
    result = (temperature * 9/5) - 459.67
    print(temperature, "Kelvin =", result, "Fahrenheit")
elif p == 15:
    result = (temperature - 273.15) * 4/5
    print(temperature, "Kelvin =", result, "Reamur")
elif p == 16:
    result = temperature * 9/5
    print(temperature, "Kelvin =", result, "Rankine")
elif p == 17:
    result = (temperature - 491.67) * 5/9
    print(temperature, "Rankine =", result, "Celsius")
elif p == 18:
    result = temperature - 459.67
    print(temperature, "Rankine =", result, "Fahrenheit")
elif p == 19:
    result = (temperature - 491.67) * 4/9
    print(temperature, "Rankine =", result, "Reamur")
elif p == 20:
    result = temperature * 5/9
    print(temperature, "Rankine =", result, "Kelvin")
else:
    print("Pilihan tidak valid")
=======
print("Konveri Suhu")
print("1. Celsius ke Fahrenheit")
print("2. Celsius ke Reamur")
print("3. Celsius ke Kelvin")
print("4. Celsius ke Rankine")
print("5. Fahrenheit ke Celsius")
print("6. Fahrenheit ke Reamur")
print("7. Fahrenheit ke Kelvin")
print("8. Fahrenheit ke Rankine")
print("9. Reamur ke Celsius")
print("10. Reamur ke Fahrenheit")
print("11. Reamur ke Kelvin")
print("12. Reamur ke Rankine")
print("13. Kelvin ke Celsius")
print("14. Kelvin ke Fahrenheit")
print("15. Kelvin ke Reamur")
print("16. Kelvin ke Rankine")
print("17. Rankine ke Celsius")
print("18. Rankine ke Fahrenheit")
print("19. Rankine ke Reamur")
print("20. Rankine ke Kelvin")

p = int(input("Masukkan Pilihan (1-20): "))
temperature = float(input("Masukkan Suhu: "))

if p == 1:
    result = (temperature * 9/5) + 32
    print(temperature, "Celsius =", result, "Fahrenheit")
elif p == 2:
    result = temperature * 4/5
    print(temperature, "Celsius =", result, "Reamur")
elif p == 3:
    result = temperature + 273.15
    print(temperature, "Celsius =", result, "Kelvin")
elif p == 4:
    result = (temperature + 273.15) * 9/5
    print(temperature, "Celsius =", result, "Rankine")
elif p == 5:
    result = (temperature - 32) * 5/9
    print(temperature, "Fahrenheit =", result, "Celsius")
elif p == 6:
    result = (temperature - 32) * 4/9
    print(temperature, "Fahrenheit =", result, "Reamur")
elif p == 7:
    result = (temperature + 459.67) * 5/9
    print(temperature, "Fahrenheit =", result, "Kelvin")
elif p == 8:
    result = temperature + 459.67
    print(temperature, "Fahrenheit =", result, "Rankine")
elif p == 9:
    result = temperature * 5/4
    print(temperature, "Reamur =", result, "Celsius")
elif p == 10:
    result = (temperature * 9/4) + 32
    print(temperature, "Reamur =", result, "Fahrenheit")
elif p == 11:
    result = (temperature * 5/4) + 273.15
    print(temperature, "Reamur =", result, "Kelvin")
elif p == 12:
    result = (temperature * 9/4) + 491.67
    print(temperature, "Reamur =", result, "Rankine")
elif p == 13:
    result = temperature - 273.15
    print(temperature, "Kelvin =", result, "Celsius")
elif p == 14:
    result = (temperature * 9/5) - 459.67
    print(temperature, "Kelvin =", result, "Fahrenheit")
elif p == 15:
    result = (temperature - 273.15) * 4/5
    print(temperature, "Kelvin =", result, "Reamur")
elif p == 16:
    result = temperature * 9/5
    print(temperature, "Kelvin =", result, "Rankine")
elif p == 17:
    result = (temperature - 491.67) * 5/9
    print(temperature, "Rankine =", result, "Celsius")
elif p == 18:
    result = temperature - 459.67
    print(temperature, "Rankine =", result, "Fahrenheit")
elif p == 19:
    result = (temperature - 491.67) * 4/9
    print(temperature, "Rankine =", result, "Reamur")
elif p == 20:
    result = temperature * 5/9
    print(temperature, "Rankine =", result, "Kelvin")
else:
    print("Pilihan tidak valid")
>>>>>>> f363c0c524fc02589f7fb6e0fc6af06df1568914:Latihan Python/konversi_suhu.py
