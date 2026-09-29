"""
KASUS 02 - PEWARISAN SIFAT (INHERITANCE)
Sistem Rental Kendaraan
"""


class Kendaraan:
    """Class induk: fondasi umum seluruh armada."""

    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def tampilkan_info(self):
        print(f"Nama      : {self.nama}")
        print(f"Merk      : {self.merk}")
        print(f"Tahun     : {self.tahun}")
        print(f"Kecepatan : {self.kecepatan} km/jam")


class Mobil(Kendaraan):
    """Turunan 1: armada roda empat."""

    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def tampilkan_info(self):
        print("[MOBIL]")
        super().tampilkan_info()
        print(f"Kursi     : {self.jumlah_kursi}")
        print("-" * 32)


class Motor(Kendaraan):
    """Turunan 2: armada roda dua."""

    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def tampilkan_info(self):
        print("[MOTOR]")
        super().tampilkan_info()
        print(f"Tipe      : {self.tipe_motor}")
        print("-" * 32)


if __name__ == "__main__":
    print("=" * 32)
    print("KASUS 02 - SISTEM RENTAL KENDARAAN")
    print("=" * 32)

    armada = [
        Mobil("Avanza", "Toyota", 2022, 160, 7),
        Mobil("Brio", "Honda", 2023, 170, 5),
        Motor("Vario 160", "Honda", 2023, 110, "Matic"),
        Motor("CB150R", "Honda", 2021, 140, "Sport"),
    ]

    for kendaraan in armada:
        kendaraan.tampilkan_info()