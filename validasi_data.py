def validasi_data(nim, ipk, sks, semester):
    error_list = []

    if not nim.isdigit() or len(nim) != 10:
        error_list.append("NIM harus 10 digit angka.")
    elif not 2000 <= int(nim[:4]) <= 2037:
        error_list.append("Tahun pada NIM harus 2000-2037.")

    if not 0.0 <= ipk <= 4.0:
        error_list.append("IPK harus antara 0.0-4.0.")

    if not 0 <= sks <= 24:
        error_list.append("SKS harus antara 0-24.")

    if not 1 <= semester <= 14:
        error_list.append("Semester harus antara 1-14.")

    return error_list


print("=== VALIDASI DATA MAHASISWA ===")

nim = input("NIM: ")
ipk = float(input("IPK: "))
sks = int(input("SKS: "))
semester = int(input("Semester: "))

errors = validasi_data(nim, ipk, sks, semester)

if len(errors) == 0:
    print("\nData valid.")
else:
    print("\nData tidak valid:")
    for error in errors:
        print("-", error)