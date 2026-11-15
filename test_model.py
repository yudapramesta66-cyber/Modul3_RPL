from models.buku_model import BukuModel

model = BukuModel()
daftar_buku = model.get_all_buku()

print("=== Daftar Buku ===")
for buku in daftar_buku:
    print(f"{buku['id_buku']}. {buku['judul']} ({buku['penulis']}, {buku['tahun_terbit']})")