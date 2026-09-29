class Pegawai:
    """Identitas pegawai."""

    def __init__(self, id_pegawai, nama, **kwargs):
        super().__init__(**kwargs)
        self.id_pegawai = id_pegawai
        self.nama = nama


class Gaji:
    """Data payroll."""

    def __init__(self, gaji, **kwargs):
        super().__init__(**kwargs)
        self.gaji = gaji


class PegawaiProyek:
    """Tanggung jawab proyek."""

    def __init__(self, nama_proyek, **kwargs):
        super().__init__(**kwargs)
        self.nama_proyek = nama_proyek


class ProjectManager(Pegawai, Gaji, PegawaiProyek):
    """Mewarisi 3 class induk sekaligus."""

    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        super().__init__(
            id_pegawai=id_pegawai,
            nama=nama,
            gaji=gaji,
            nama_proyek=nama_proyek,
        )

    def tampilkan_data(self):
        print(f"ID Pegawai : {self.id_pegawai}")
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : Rp{self.gaji:,.0f}".replace(",", "."))
        print(f"Proyek     : {self.nama_proyek}")
        print("-" * 32)


if __name__ == "__main__":
    print("=" * 32)
    print("KASUS 03 - SISTEM MANAJEMEN PEGAWAI")
    print("=" * 32)

    pm = ProjectManager("PM-001", "Dewi Anggraini", 15_000_000, "Aplikasi Kampus Digital")
    pm.tampilkan_data()

    print("Urutan pewarisan (MRO):")
    print(" -> ".join(cls.__name__ for cls in ProjectManager.__mro__))
