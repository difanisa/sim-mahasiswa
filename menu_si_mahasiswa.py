while True:
    print("\n=== MENU SI MAHASISWA ===")
    print("1. Status Mahasiswa")
    print("2. Diskon Biaya Kuliah")
    print("3. Peringatan Stok")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nim = input("NIM: ")
        nama = input("Nama: ")
        ipk = float(input("IPK: "))
        sks = int(input("SKS: "))

        if ipk < 1.5:
            status = "Tidak Aktif"
        elif ipk < 2.0:
            status = "Peringatan"
        elif sks >= 18:
            status = "Aktif"
        else:
            status = "Tidak Aktif"

        print(f"\nNIM: {nim}")
        print(f"Nama: {nama}")
        print(f"IPK: {ipk}")
        print(f"SKS: {sks}")
        print(f"Status: {status}")

    elif pilihan == "2":
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

    elif pilihan == "3":
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

        total_nilai = 0
        jumlah_aman = 0
        jumlah_waspada = 0
        jumlah_rendah = 0
        jumlah_habis = 0

        for item in barang:
            stok = item["stok"]
            nilai = item["harga"] * stok
            total_nilai += nilai

            if stok > 20:
                status = "Aman"
                rekomendasi = "Stok aman"
                jumlah_aman += 1
            elif stok >= 11:
                status = "Waspada"
                rekomendasi = "Pantau stok"
                jumlah_waspada += 1
            elif stok >= 1:
                status = "Rendah"
                rekomendasi = "Segera restock"
                jumlah_rendah += 1
            else:
                status = "Habis"
                rekomendasi = "Segera restock"
                jumlah_habis += 1

            print(f"\n{item['nama']}: {status} (stok {stok})")
            print(f"Rekomendasi: {rekomendasi}")
            print(f"Nilai inventaris: Rp{nilai:,.0f}")

        print("\n=== RINGKASAN ===")
        print(f"Total nilai inventaris: Rp{total_nilai:,.0f}")
        print(f"Jumlah stok aman: {jumlah_aman}")
        print(f"Jumlah stok waspada: {jumlah_waspada}")
        print(f"Jumlah stok rendah: {jumlah_rendah}")
        print(f"Jumlah barang habis: {jumlah_habis}")

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")