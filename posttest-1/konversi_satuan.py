print("LOGIN")
# input data
nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
kelas = input("Masukkan kelas: ")

# cetak data
print("\n~~~~~~~~~~~~~~~~~~~")
print(f"Nama: {nama}")
print(f"NIM: {nim}")
print(f"kelas: {kelas}")
print("~~~~~~~~~~~~~~~~~~~\n")

print("PROGRAM KONVERSI SATUAN MASSA KILOGRAM")
# input berat
kg = float(input("Masukkan berat dalam kilogram: "))

# input satuan
print("\nSatuan massa:")
print("1. Pounds (lb)")
print("2. Ounce (ons)")
print("3. Gram (g)")
pilihan = input("Masukkan pilihan satuan (1/2/3): ")
print("") # buat ngasih jarak aja

# konversi ke pounds
if pilihan == "1":
    berat = kg * 2.20462
    print(f"{kg} kilogram sama dengan {berat} pounds")
# konversi ke ons
elif pilihan == "2":
    berat = kg * 35.274
    print(f"{kg} kilogram sama dengan {berat} ons")
# konversi ke gram
elif pilihan == "3":
    berat = kg * 1000
    print(f"{kg} kilogram sama dengan {berat} gram")
# jika pilihan bukan 1/2/3
else:
    print("Pilihan tidak valid! Pilih 1, 2, atau 3")
