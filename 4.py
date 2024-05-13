# Konversi bilangan dari nomor handphone dan NIM

# Contoh nomor handphone
nomor_hp = "081234567890"
enam_angka_terakhir = nomor_hp[-6:]

# Konversi ke biner, heksa, dan oktal
biner = bin(int(enam_angka_terakhir))
heksa = hex(int(enam_angka_terakhir))
oktal = oct(int(enam_angka_terakhir))

print(f"Nomor handphone: {nomor_hp}")
print(f"Enam angka terakhir: {enam_angka_terakhir}")
print("\nKonversi dari enam angka terakhir nomor HP:")
print(f"Biner: {biner}")
print(f"Heksa: {heksa}")
print(f"Oktal: {oktal}")

# Contoh NIM
nim_asli = ["23090156", "23090121", "23090086", "23090119", "23090120"]
nim_modifikasi = []

# Modifikasi NIM dengan mengganti 3 angka terakhir
for nim in nim_asli:
    nim_baru = nim[:-3] + "789"  # Mengganti 3 angka terakhir dengan '789'
    nim_modifikasi.append(nim_baru)

print("\nNIM asli dan NIM yang telah dimodifikasi:")
for asli, modif in zip(nim_asli, nim_modifikasi):
    print(f"Asli: {asli}, Modifikasi: {modif}")

# Konversi ke biner, heksa, dan oktal
print("\nKonversi dari NIM asli:")
for nim in nim_asli:
    biner = bin(int(nim))
    heksa = hex(int(nim))
    oktal = oct(int(nim))
    print(f"NIM asli: {nim}, Biner: {biner}, Heksa: {heksa}, Oktal: {oktal}")

# Konversi ke biner, heksa, dan oktal
print("\nKonversi dari NIM yang telah dimodifikasi:")
for nim in nim_modifikasi:
    biner = bin(int(nim))
    heksa = hex(int(nim))
    oktal = oct(int(nim))
    print(f"NIM dimodifikasi: {nim}, Biner : {biner}, Heksa : {heksa}, Oktal : {oktal}")