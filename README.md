# Sistem Manajemen Perpustakaan (Desktop Python MVC)

## Deskripsi Singkat Aplikasi
**Sistem Manajemen Perpustakaan** adalah aplikasi desktop berbasis arsitektur **Model-View-Controller (MVC)** yang dibangun menggunakan bahasa pemrograman Python, pustaka antarmuka modern **CustomTkinter**, dan basis data relasional **MySQL**[cite: 6]. Aplikasi ini dilengkapi mekanisme **Autentikasi** menggunakan enkripsi satu arah (*password hashing*) **SHA-256** serta **Otorisasi berbasis peran (Role-Based Access Control / RBAC)** yang membedakan hak akses antara **Admin** (kelola penuh data buku dan anggota) dan **Anggota** (mode baca katalog buku).

## Struktur Direktori MVC
```text
Modul3_RPL/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml        # Konfigurasi CI otomatis GitHub Actions
├── config/
│   └── database.py                # Konfigurasi koneksi MySQL
├── controllers/
│   ├── auth_controller.py         # Pengatur alur login dan sesi pengguna
│   ├── buku_controller.py         # Penghubung View & Model Buku serta kontrol RBAC
│   └── anggota_controller.py      # Penghubung View & Model Anggota
├── models/
│   ├── buku_model.py              # Operasi CRUD tabel buku
│   ├── anggota_model.py           # Operasi CRUD tabel anggota
│   └── user_model.py              # Hashing SHA-256, registrasi, dan verifikasi user
├── views/
│   ├── login_view.py              # Antarmuka jendela login
│   ├── buku_view.py               # Antarmuka manajemen koleksi buku
│   └── anggota_view.py            # Antarmuka manajemen data anggota
├── tests/
│   ├── test_auth.py               # Unit test autentikasi & hashing SHA-256
│   └── test_buku.py               # Unit test controller buku
├── .gitignore                     # Daftar file/folder yang diabaikan Git
├── main.py                        # Titik masuk utama aplikasi
├── requirements.txt               # Daftar dependensi pustaka Python
└── README.md                      # Dokumentasi teknis proyek
```

## Panduan Instalasi & Konfigurasi Database MySQL

### 1. Konfigurasi Database MySQL (Laragon)
1. Buka aplikasi **Laragon** dan jalankan layanan **MySQL** (`Start All`)[cite: 6].
2. Masuk ke terminal MySQL (`mysql -u root -p`), lalu jalankan kueri SQL berikut[cite: 6]:
   ```sql
   CREATE DATABASE db_perpustakaanrpl;
   USE db_perpustakaanrpl;

   CREATE TABLE buku (
       id_buku INT PRIMARY KEY AUTO_INCREMENT,
       judul VARCHAR(100) NOT NULL,
       penulis VARCHAR(100) NOT NULL,
       tahun_terbit YEAR
   );

   CREATE TABLE anggota (
       id_anggota INT PRIMARY KEY AUTO_INCREMENT,
       nama VARCHAR(100) NOT NULL,
       alamat TEXT
   );

   CREATE TABLE users (
       id_user INT PRIMARY KEY AUTO_INCREMENT,
       username VARCHAR(50) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL,
       role ENUM('admin', 'anggota') NOT NULL DEFAULT 'anggota'
   );

   INSERT INTO users (username, password, role) VALUES
   ('petugas', SHA2('admin123', 256), 'admin'),
   ('mahasiswa', SHA2('user123', 256), 'anggota');
   ```
3. Sesuaikan parameter koneksi di `config/database.py` apabila kredensial MySQL lokal berbeda (`host="localhost"`, `user="root"`, `password=""`, `database="db_perpustakaanrpl"`).

### 2. Instalasi Lingkungan Python
```bash
git clone [https://github.com/yudapramesta66-cyber/Modul3_RPL.git](https://github.com/yudapramesta66-cyber/Modul3_RPL.git)
cd Modul3_RPL
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

## Cara Menjalankan Aplikasi

### Opsi A: Melalui Kode Sumber Python
Pastikan layanan MySQL di Laragon aktif dan `(env)` menyala, lalu jalankan[cite: 6]:
```bash
python main.py
```

### Opsi B: Menggunakan File Eksekusi Mandiri (`.exe`)
1. Pastikan layanan **MySQL** pada Laragon sudah aktif[cite: 6].
2. Unduh berkas `AplikasiPerpustakaan.exe` pada halaman **Releases** repositori ini (atau buka folder `dist/` setelah *build* PyInstaller).
3. Klik dua kali berkas **`AplikasiPerpustakaan.exe`**[cite: 6].
4. Masuk menggunakan akun uji coba:
   - **Admin:** `petugas` / `admin123`[cite: 6]
   - **Anggota:** `mahasiswa` / `user123`[cite: 6]