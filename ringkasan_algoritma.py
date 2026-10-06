mahasiswa = [
    {"nama": "Andi", "ipk": 3.5, "sks": 20},
    {"nama": "Budi", "ipk": 1.8, "sks": 15},
    {"nama": "Cici", "ipk": 3.9, "sks": 22},
    {"nama": "Dodi", "ipk": 2.5, "sks": 18},
    {"nama": "Eka", "ipk": 1.2, "sks": 12}
]

diskon = [25, 20, 15, 10, 5]

barang = [
    {"nama": "Laptop", "stok": 25},
    {"nama": "Mouse", "stok": 18},
    {"nama": "Keyboard", "stok": 10},
    {"nama": "Monitor", "stok": 5},
    {"nama": "Headset", "stok": 0},
    {"nama": "Flashdisk", "stok": 30},
    {"nama": "Webcam", "stok": 7},
    {"nama": "Kabel HDMI", "stok": 15}
]

# Persentase mahasiswa aktif vs tidak aktif
aktif = 0
tidak_aktif = 0

for mhs in mahasiswa:
    if mhs["ipk"] >= 2.0 and mhs["sks"] >= 18:
        aktif += 1
    else:
        tidak_aktif += 1

total_mahasiswa = len(mahasiswa)
persen_aktif = aktif / total_mahasiswa * 100
persen_tidak_aktif = tidak_aktif / total_mahasiswa * 100

# Rata-rata diskon
rata_diskon = sum(diskon) / len(diskon)

# Persentase item yang perlu restock
restock = 0

for item in barang:
    if item["stok"] <= 10:
        restock += 1

persen_restock = restock / len(barang) * 100

print("\n=== RINGKASAN ALGORITMA ===")
print(f"{'Indikator':<35} {'Hasil':>10}")
print("-" * 47)
print(f"{'Mahasiswa Aktif':<35} {persen_aktif:>9.2f}%")
print(f"{'Mahasiswa Tidak Aktif':<35} {persen_tidak_aktif:>9.2f}%")
print(f"{'Rata-rata Diskon':<35} {rata_diskon:>9.2f}%")
print(f"{'Item Perlu Restock':<35} {persen_restock:>9.2f}%")