class mahasiswa :
    def __init__(self, nama, nim, jurusan, nilai):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = nilai

    def cek_status(self):
        if self.nilai >= 75 :
            return "lulus"
        else:
            return "tidak lulus"

    def cetak_profil(self):
        print(f"nama    :{self.nama}")
        print(f"nim     :{self.nim}")
        print(f"jurusan :{self.jurusan}")
        print(f"nilai   :{self.nilai}")
        print(f"status  :{self.cek_status()}")
        print("-" *35)


mahasiswa1 = mahasiswa("Andi Wijaya", "23010101", "Teknik Informatika", 85)
mahasiswa2 = mahasiswa("Siti Rahma", "23010102", "Sistem Informasi", 72)
mahasiswa3 = mahasiswa("Budi Santoso", "23010103", "Sains Data", 90)


print("=" * 12, "DATA MAHASISWA", "=" * 12)
mahasiswa1.cetak_profil()
mahasiswa2.cetak_profil()
mahasiswa3.cetak_profil()