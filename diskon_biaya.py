biaya_kuliah = float(input("Biaya kuliah: "))
anak_pegawai = input("Anak pegawai? (y/n): ")
ipk = float(input("IPK: "))
tepat_waktu = input("Pembayaran tepat waktu? (y/n): ")

if anak_pegawai == "y":
    diskon_utama = 25
elif ipk >= 3.8:
    diskon_utama = 20
elif ipk >= 3.5:
    diskon_utama = 15
elif ipk >= 3.0:
    diskon_utama = 10
else:
    diskon_utama = 0

diskon_tepat_waktu = 5 if tepat_waktu == "y" else 0

total_diskon = diskon_utama + diskon_tepat_waktu

potongan = biaya_kuliah * total_diskon / 100
biaya_akhir = biaya_kuliah - potongan

print(f"Total diskon: {total_diskon}%")
print(f"Potongan: Rp{potongan:,.0f}")
print(f"Biaya akhir: Rp{biaya_akhir:,.0f}")