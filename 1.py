# Membuat daftar nama mahasiswa dengan nomor urut
daftar_mahasiswa = [
    "(01) UTBAH ABDURRAHMAN",
    "(02) A FAHRI PUTRA PRATAMA",
    "(03) ABDULLAH ROBITHUL HASAN",
    "(04) ACHMAD MUNDAKIR",
    "(05) AHMAD MAULANA FAIZ",
    "(06) AKMAL KURNIAWAN",
    "(07) ALBAR ABDULLAH FIRDAUS",
    "(08) ATHA DION SAPUTRA",
    "(09) BINTANG AJI SAPUTRA",
    "(10) BRIYAN DWI SEPTIAN",
    "(11) DINDA DESTRIYANI HERNAWATI",
    "(12) EVAN ALAMBANA",
    "(13) FAJAR ZIDAN MUZAKKI",
    "(14) FAJRINA NURHALIZA",
    "(15) FARELL PRIA ADHITAMA",
    "(16) HILMAN BINTANG ARDHANI",
    "(17) HUSAIN MULYANSYAH",
    "(18) IHSAN NAFIS HIDAYAT",
    "(19) IZATH",
    "(20) MOHAMAD ARKAN RAMADHANNY"
    ]

# Menampilkan jumlah dan daftar nama mahasiswa
print("\n20 daftar mahasiswa:")
print("--------------------")
for mahasiswa in daftar_mahasiswa:
    print(f"{mahasiswa}")

# Menambahkan 5 nama mahasiswa baru ke dalam daftar
daftar_mahasiswa.extend([
    "(21) MUAMMAR HILMI AZIZ",
    "(22) MUHAMMAD IDRIS MARZUKI",
    "(23) MUHAMMAD IQBAL SAPUTRA",
    "(24) MUHAMMAD RIZQI ABDI GIFFARI",
    "(25) BAGAS ABIYU KUMARA"
    ])
# Menampilkan jumlah dan daftar nama mahasiswa baru yang ditambahkan
print("\n5 nama mahasiswa baru:")
print("--------------------")
for mahasiswa_baru in daftar_mahasiswa[-5:]:
    print(f"{mahasiswa_baru}")