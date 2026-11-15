from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self, model=None, view=None):
        self.model = model if model else AnggotaModel()
        self.view = view if view else AnggotaView()

        self.view.btn_simpan.configure(command=self.simpan_anggota)
        self.view.btn_perbarui.configure(command=self.perbarui_anggota)
        self.view.btn_hapus.configure(command=self.hapus_anggota)
        self.view.tree.bind("<<TreeviewSelect>>", self.pilih_baris_anggota)

        self.muat_data_anggota()

    def muat_data_anggota(self):
        data = self.model.get_all_anggota()
        self.view.tampilkan_data(data)

    def pilih_baris_anggota(self, event=None):
        baris = self.view.get_selected_anggota()
        if baris:
            _, nama, alamat = baris
            self.view.set_input_data(nama, alamat)

    def simpan_anggota(self):
        nama, alamat = self.view.get_input_data()
        if not nama or not alamat:
            self.view.show_error("Nama dan alamat harus diisi!")
            return

        if self.model.create_anggota(nama, alamat):
            self.view.show_info("Data anggota berhasil disimpan!")
            self.view.clear_input()
            self.muat_data_anggota()
        else:
            self.view.show_error("Gagal menyimpan data anggota.")

    def perbarui_anggota(self):
        baris = self.view.get_selected_anggota()
        if not baris:
            self.view.show_error("Pilih baris anggota pada tabel terlebih dahulu!")
            return

        id_anggota = baris[0]
        nama, alamat = self.view.get_input_data()
        if not nama or not alamat:
            self.view.show_error("Nama dan alamat harus diisi!")
            return

        if self.model.update_anggota(id_anggota, nama, alamat):
            self.view.show_info("Data anggota berhasil diperbarui!")
            self.view.clear_input()
            self.muat_data_anggota()
        else:
            self.view.show_error("Gagal memperbarui data anggota.")

    def hapus_anggota(self):
        baris = self.view.get_selected_anggota()
        if not baris:
            self.view.show_error("Pilih baris anggota yang akan dihapus pada tabel!")
            return

        id_anggota, nama = baris[0], baris[1]
        if self.view.ask_confirm(f"Yakin ingin menghapus anggota '{nama}'?"):
            if self.model.delete_anggota(id_anggota):
                self.view.show_info("Data anggota berhasil dihapus!")
                self.view.clear_input()
                self.muat_data_anggota()
            else:
                self.view.show_error("Gagal menghapus data anggota.")

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    app = AnggotaController()
    app.run()