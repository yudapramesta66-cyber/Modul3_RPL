from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, model=None, view=None, user_role="admin"):
        self.model = model if model else BukuModel()
        self.view = view if view else BukuView()
        self.user_role = user_role

        self.view.title(f"Sistem Manajemen Perpustakaan - [{self.user_role.upper()}]")

        # Tombol Logout aktif untuk semua peran (admin maupun anggota)
        self.view.btn_logout.configure(command=self.logout)

        # Penerapan aturan otorisasi (RBAC)
        if self.user_role != "admin":
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")
            self.view.btn_simpan.configure(
                state="disabled",
                text="Mode Baca Saja (Anggota)",
                fg_color="#6c757d"
            )
            self.view.btn_perbarui.configure(state="disabled", fg_color="#6c757d")
            self.view.btn_hapus.configure(state="disabled", fg_color="#6c757d")
        else:
            self.view.btn_simpan.configure(command=self.simpan_buku)
            self.view.btn_perbarui.configure(command=self.perbarui_buku)
            self.view.btn_hapus.configure(command=self.hapus_buku)
            self.view.tree.bind("<<TreeviewSelect>>", self.pilih_baris_buku)

        self.muat_data_buku()

    def muat_data_buku(self):
        data = self.model.get_all_buku()
        self.view.tampilkan_data(data)

    def pilih_baris_buku(self, event=None):
        baris = self.view.get_selected_buku()
        if baris:
            _, judul, penulis, tahun = baris
            self.view.set_input_data(judul, penulis, tahun)

    def simpan_buku(self):
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

    def perbarui_buku(self):
        baris = self.view.get_selected_buku()
        if not baris:
            self.view.show_error("Pilih baris buku pada tabel terlebih dahulu!")
            return

        id_buku = baris[0]
        judul, penulis, tahun = self.view.get_input_data()
        if not judul or not penulis or not tahun:
            self.view.show_error("Semua kolom harus diisi!")
            return

        if self.model.update_buku(id_buku, judul, penulis, tahun):
            self.view.show_info("Data buku berhasil diperbarui!")
            self.view.clear_input()
            self.muat_data_buku()
        else:
            self.view.show_error("Gagal memperbarui data buku.")

    def hapus_buku(self):
        baris = self.view.get_selected_buku()
        if not baris:
            self.view.show_error("Pilih baris buku yang akan dihapus pada tabel!")
            return

        id_buku, judul = baris[0], baris[1]
        if self.view.ask_confirm(f"Yakin ingin menghapus buku '{judul}'?"):
            if self.model.delete_buku(id_buku):
                self.view.show_info("Data buku berhasil dihapus!")
                self.view.clear_input()
                self.muat_data_buku()
            else:
                self.view.show_error("Gagal menghapus data buku.")

    def logout(self):
        from controllers.auth_controller import AuthController
        self.view.destroy()
        auth_app = AuthController()
        auth_app.run()

    def run(self):
        self.view.mainloop()