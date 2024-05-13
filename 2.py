# a. Anda suka gemar Piknik atau baca buku
# Pernyataan simbolik: P v Q
# Dimana P: Anda suka gemar Piknik
#       Q: Anda suka baca buku
# Menggunakan hukum De Morgan, pernyataan ekivalen:
# ¬(¬P ∧ ¬Q)

# b. Dosen Teknik Informatika terdiri dari perempuan dan laki-laki
# Pernyataan simbolik: R ∧ S
# Dimana R: Dosen Teknik Informatika adalah perempuan
#       S: Dosen Teknik Informatika adalah laki-laki
# Menggunakan hukum De Morgan, pernyataan ekivalen:
# ¬(¬R v ¬S)

# Implementasi dalam kode (contoh sederhana untuk demonstrasi logika):
def pernyataan_logika():
    # Pernyataan a
    suka_piknik = True  # Misalkan Anda suka piknik
    suka_baca_buku = False  # Misalkan Anda tidak suka baca buku
    pernyataan_a = suka_piknik or suka_baca_buku
    ekivalen_a = not (not suka_piknik and not suka_baca_buku)

    # Pernyataan b
    dosen_perempuan = True  # Misalkan ada dosen perempuan
    dosen_laki_laki = True  # Misalkan ada dosen laki-laki
    pernyataan_b = dosen_perempuan and dosen_laki_laki
    ekivalen_b = not (not dosen_perempuan or not dosen_laki_laki)

    print("Pernyataan A (suka piknik atau baca buku):", pernyataan_a)
    print("Pernyataan A ekivalen (menggunakan hukum De Morgan):", ekivalen_a)
    print("Pernyataan B (dosen perempuan dan laki-laki):", pernyataan_b)
    print("Pernyataan B ekivalen (menggunakan hukum De Morgan):", ekivalen_b)

pernyataan_logika()