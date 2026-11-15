from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, model=None, view=None):
        self.model = model if model else BukuModel()
        self.view = view if view else BukuView()

        # Binding event tombol Simpan Data ke event handler
        self.view.btn_simpan.configure(command=self.simpan_buku)
        self.muat_data_buku()

    def muat_data_buku(self):
        data = self.model.get_all_buku()
        self.view.tampilkan_data(data)

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

    def run(self):
        self.view.mainloop()