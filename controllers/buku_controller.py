from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, model=None, view=None, user_role="admin"):
        self.model = model if model else BukuModel()
        self.view = view if view else BukuView()
        self.user_role = user_role

        # Tampilkan peran aktif pada judul jendela
        self.view.title(f"Sistem Manajemen Perpustakaan - [{self.user_role.upper()}]")

        # Penerapan Role-Based Access Control (RBAC)
        if self.user_role != "admin":
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")
            self.view.btn_simpan.configure(
                state="disabled",
                text="Mode Baca Saja (Anggota)",
                fg_color="#6c757d"
            )
        else:
            self.view.btn_simpan.configure(command=self.simpan_buku)

        self.muat_data_buku()

    def muat_data_buku(self):
        data = self.model.get_all_buku()
        self.view.tampilkan_data(data)

    def simpan_buku(self):
        if self.user_role != "admin":
            self.view.show_error("Akses ditolak! Hanya admin yang dapat menambah data buku.")
            return

        judul, penulis, tahun = self.view.get_input_data()
        if not judul or not penulis or not tahun:
            self.view.show_error("Semua kolom harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            self.view.show_info("Data buku berhasil disimpan!")
            self.view.clear_input()
            self.muat_data_buku()
        else:
            self.view.show_error("Gagal menyimpan data ke database.")

    def run(self):
        self.view.mainloop()