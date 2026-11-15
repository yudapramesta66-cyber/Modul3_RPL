import customtkinter as ctk
from tkinter import ttk, messagebox

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan - Data Anggota")
        self.geometry("820x450")
        ctk.set_appearance_mode("System")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # === PANEL KIRI: FORM INPUT DATA ANGGOTA ===
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.label_form = ctk.CTkLabel(
            self.frame_kiri, text="Form Input Data Anggota", font=("Arial", 16, "bold")
        )
        self.label_form.pack(pady=(15, 10))

        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Nama Anggota", width=220
        )
        self.entry_nama.pack(pady=8, padx=15)

        self.entry_alamat = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Alamat", width=220
        )
        self.entry_alamat.pack(pady=8, padx=15)

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

        # === PANEL KANAN: TABEL DAFTAR ANGGOTA ===
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=(0, 15), pady=15, sticky="nsew")

        self.label_tabel = ctk.CTkLabel(
            self.frame_kanan, text="Daftar Anggota Perpustakaan", font=("Arial", 16, "bold")
        )
        self.label_tabel.pack(pady=(15, 10))

        kolom = ("id", "nama", "alamat")
        self.tree = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=14)
        self.tree.heading("id", text="ID")
        self.tree.heading("nama", text="Nama Anggota")
        self.tree.heading("alamat", text="Alamat")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("nama", width=180)
        self.tree.column("alamat", width=220)
        self.tree.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    def get_input_data(self):
        return (
            self.entry_nama.get().strip(),
            self.entry_alamat.get().strip(),
        )

    def set_input_data(self, nama, alamat):
        self.clear_input()
        self.entry_nama.insert(0, str(nama))
        self.entry_alamat.insert(0, str(alamat))

    def clear_input(self):
        self.entry_nama.delete(0, "end")
        self.entry_alamat.delete(0, "end")

    def get_selected_anggota(self):
        selected = self.tree.selection()
        if not selected:
            return None
        return self.tree.item(selected[0], "values")

    def tampilkan_data(self, data_anggota):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for anggota in data_anggota:
            self.tree.insert(
                "", "end",
                values=(anggota["id_anggota"], anggota["nama"], anggota["alamat"])
            )

    def show_info(self, pesan):
        messagebox.showinfo("Informasi", pesan)

    def show_error(self, pesan):
        messagebox.showerror("Peringatan", pesan)

    def ask_confirm(self, pesan):
        return messagebox.askyesno("Konfirmasi", pesan)