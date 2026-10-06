barang = [
    {"nama": "Laptop", "harga": 8000000, "stok": 25},
    {"nama": "Mouse", "harga": 150000, "stok": 18},
    {"nama": "Keyboard", "harga": 300000, "stok": 10},
    {"nama": "Monitor", "harga": 2000000, "stok": 5},
    {"nama": "Headset", "harga": 250000, "stok": 0},
    {"nama": "Flashdisk", "harga": 100000, "stok": 30},
    {"nama": "Webcam", "harga": 500000, "stok": 7},
    {"nama": "Kabel HDMI", "harga": 75000, "stok": 15}
]
for item in barang:
    stok = item["stok"]

    if stok > 20:
        status = "Aman"
    elif stok >= 11:
        status = "Waspada"
    elif stok >= 1:
        status = "Rendah"
    else:
        status = "Habis"

    print(f"{item['nama']}: {status} (stok {stok})")

    nilai = item["harga"] * item["stok"]

    if stok <= 10:
        rekomendasi = "Segera restock"
    elif stok <= 20:
        rekomendasi = "Pantau stok"
    else:
        rekomendasi = "Stok aman"

    print(f"Rekomendasi: {rekomendasi}")
    print(f"Nilai inventaris: Rp{nilai:,.0f}")

    total_nilai = 0
jumlah_aman = 0
jumlah_waspada = 0
jumlah_rendah = 0
jumlah_habis = 0

for item in barang:
    stok = item["stok"]
    total_nilai += item["harga"] * stok

    if stok > 20:
        jumlah_aman += 1
    elif stok >= 11:
        jumlah_waspada += 1
    elif stok >= 1:
        jumlah_rendah += 1
    else:
        jumlah_habis += 1

print("\n=== RINGKASAN ===")
print(f"Total nilai inventaris: Rp{total_nilai:,.0f}")
print(f"Jumlah stok aman: {jumlah_aman}")
print(f"Jumlah stok waspada: {jumlah_waspada}")
print(f"Jumlah stok rendah: {jumlah_rendah}")
print(f"Jumlah barang habis: {jumlah_habis}")