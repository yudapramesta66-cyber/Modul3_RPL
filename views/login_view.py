import customtkinter as ctk
from tkinter import messagebox

class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Sistem Manajemen Perpustakaan")
        self.geometry("380x290")
        self.resizable(False, False)
        ctk.set_appearance_mode("System")

        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(fill="both", expand=True, padx=20, pady=20)

        self.label_judul = ctk.CTkLabel(
            self.frame_login,
            text="Login Sistem Perpustakaan",
            font=("Arial", 18, "bold")
        )
        self.label_judul.pack(pady=(20, 15))

        self.entry_username = ctk.CTkEntry(
            self.frame_login,
            placeholder_text="Masukkan Username",
            width=250
        )
        self.entry_username.pack(pady=8)

        self.entry_password = ctk.CTkEntry(
            self.frame_login,
            placeholder_text="Masukkan Password",
            show="*",
            width=250
        )
        self.entry_password.pack(pady=8)

        self.btn_login = ctk.CTkButton(
            self.frame_login,
            text="Login",
            fg_color="#1f6aa5",
            hover_color="#144870",
            width=250
        )
        self.btn_login.pack(pady=(15, 10))

    def get_credentials(self):
        return (
            self.entry_username.get().strip(),
            self.entry_password.get().strip()
        )

    def show_info(self, pesan):
        messagebox.showinfo("Informasi", pesan)

    def show_error(self, pesan):
        messagebox.showerror("Login Gagal", pesan)