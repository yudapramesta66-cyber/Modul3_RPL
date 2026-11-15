from config.database import Database
from mysql.connector import Error

class BukuModel:
    def __init__(self):
        self.db = Database()

    def get_all_buku(self):
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM buku")
            return cursor.fetchall()
        except Error as e:
            print(f"Gagal mengambil data buku: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def create_buku(self, judul, penulis, tahun_terbit):
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            query = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
            cursor.execute(query, (judul, penulis, tahun_terbit))
            conn.commit()
            return True
        except Error as e:
            conn.rollback()
            print(f"Gagal menambah buku: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            query = "UPDATE buku SET judul=%s, penulis=%s, tahun_terbit=%s WHERE id_buku=%s"
            cursor.execute(query, (judul, penulis, tahun_terbit, id_buku))
            conn.commit()
            return True
        except Error as e:
            conn.rollback()
            print(f"Gagal mengubah buku: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def delete_buku(self, id_buku):
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            query = "DELETE FROM buku WHERE id_buku=%s"
            cursor.execute(query, (id_buku,))
            conn.commit()
            return True
        except Error as e:
            conn.rollback()
            print(f"Gagal menghapus buku: {e}")
            return False
        finally:
            cursor.close()
            conn.close()