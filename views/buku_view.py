import customtkinter as ctk
from tkinter import ttk, messagebox

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("850x500")
        ctk.set_appearance_mode("System")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # === PANEL KIRI: FORM INPUT DATA BUKU ===
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.label_form = ctk.CTkLabel(
            self.frame_kiri, text="Form Input Data Buku", font=("Arial", 16, "bold")
        )
        self.label_form.pack(pady=(15, 10))

        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Judul Buku", width=220
        )
        self.entry_judul.pack(pady=8, padx=15)

        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Nama Penulis", width=220
        )
        self.entry_penulis.pack(pady=8, padx=15)

        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Tahun Terbit", width=220
        )
        self.entry_tahun.pack(pady=8, padx=15)

        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="#28a745",
            hover_color="#218838",
            width=220
        )
        self.btn_simpan.pack(pady=(15, 6), padx=15)

        self.btn_perbarui = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data",
            fg_color="#ffc107",
            hover_color="#e0a800",
            text_color="black",
            width=220
        )
        self.btn_perbarui.pack(pady=6, padx=15)

        self.btn_hapus = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data",
            fg_color="#dc3545",
            hover_color="#c82333",
            width=220
        )
        self.btn_hapus.pack(pady=6, padx=15)

        self.btn_logout = ctk.CTkButton(
            self.frame_kiri,
            text="Logout",
            fg_color="#495057",
            hover_color="#343a40",
            width=220
        )
        self.btn_logout.pack(side="bottom", pady=15, padx=15)

        # === PANEL KANAN: TABEL DAFTAR KOLEKSI BUKU ===
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=(0, 15), pady=15, sticky="nsew")

        self.label_tabel = ctk.CTkLabel(
            self.frame_kanan, text="Daftar Koleksi Buku", font=("Arial", 16, "bold")
        )
        self.label_tabel.pack(pady=(15, 10))

        kolom = ("id", "judul", "penulis", "tahun")
        self.tree = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=14)
        self.tree.heading("id", text="ID")
        self.tree.heading("judul", text="Judul Buku")
        self.tree.heading("penulis", text="Penulis")
        self.tree.heading("tahun", text="Tahun")

        self.tree.column("id", width=40, anchor="center")
        self.tree.column("judul", width=180)
        self.tree.column("penulis", width=140)
        self.tree.column("tahun", width=70, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    def get_input_data(self):
        return (
            self.entry_judul.get().strip(),
            self.entry_penulis.get().strip(),
            self.entry_tahun.get().strip(),
        )

    def set_input_data(self, judul, penulis, tahun):
        self.clear_input()
        self.entry_judul.insert(0, str(judul))
        self.entry_penulis.insert(0, str(penulis))
        self.entry_tahun.insert(0, str(tahun))

    def clear_input(self):
        self.entry_judul.delete(0, "end")
        self.entry_penulis.delete(0, "end")
        self.entry_tahun.delete(0, "end")

    def get_selected_buku(self):
        selected = self.tree.selection()
        if not selected:
            return None
        return self.tree.item(selected[0], "values")

    def tampilkan_data(self, data_buku):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for buku in data_buku:
            self.tree.insert(
                "", "end",
                values=(buku["id_buku"], buku["judul"], buku["penulis"], buku["tahun_terbit"])
            )

    def show_info(self, pesan):
        messagebox.showinfo("Informasi", pesan)

    def show_error(self, pesan):
        messagebox.showerror("Peringatan", pesan)

    def ask_confirm(self, pesan):
        return messagebox.askyesno("Konfirmasi", pesan)