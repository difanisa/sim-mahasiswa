import pytest
from src.models import Mahasiswa, DaftarMahasiswa


class TestMahasiswa:

    def test_nim_kosong(self):
        with pytest.raises(ValueError):
            Mahasiswa("", "Test", "SI", 2024, 3.0)

    def test_nama_sangat_panjang(self):
        nama_panjang = "A" * 1000
        mhs = Mahasiswa("2024SI006", nama_panjang, "SI", 2024, 3.0)

        assert mhs.nama == nama_panjang
        
    def test_mahasiswa_valid(self):
        mhs = Mahasiswa(
            "2024SI001",
            "Andi",
            "Sistem Informasi",
            2024,
            3.50
        )

        assert mhs.nim == "2024SI001"
        assert mhs.nama == "Andi"
        assert mhs.ipk == 3.50

    def test_nim_tidak_valid(self):
        with pytest.raises(ValueError):
            Mahasiswa("abc", "Test", "SI", 2024, 3.0)

    def test_ipk_diluar_range(self):
        with pytest.raises(ValueError):
            Mahasiswa("2024SI002", "Test", "SI", 2024, 5.0)

    def test_ipk_batas_bawah(self):
        mhs = Mahasiswa("2024SI004", "Citra", "SI", 2024, 0.0)
        assert mhs.ipk == 0.0

    def test_ipk_batas_atas(self):
        mhs = Mahasiswa("2024SI005", "Dina", "SI", 2024, 4.0)
        assert mhs.ipk == 4.0
    
    def test_hapus_nim_tidak_ada(self):
        db = DaftarMahasiswa()
        assert db.hapus("NIM-TIDAK-ADA") is False

    def test_cari_nim_tidak_ada(self):
        db = DaftarMahasiswa()
        assert db.cari("NIM-TIDAK-ADA") is None


class TestDaftarMahasiswa:

    def test_tambah_dan_cari(self):
        db = DaftarMahasiswa()
        mhs = Mahasiswa("2024SI001", "Andi", "SI", 2024)

        db.tambah(mhs)

        assert db.cari("2024SI001") == mhs
        assert db.jumlah == 1

    def test_nim_duplikat(self):
        db = DaftarMahasiswa()

        m1 = Mahasiswa("2024SI001", "Andi", "SI", 2024)
        m2 = Mahasiswa("2024SI001", "Budi", "SI", 2024)

        db.tambah(m1)

        with pytest.raises(ValueError):
            db.tambah(m2)