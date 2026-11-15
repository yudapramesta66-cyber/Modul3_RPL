from config.database import Database
from mysql.connector import Error

class AnggotaModel:
    def __init__(self):
        self.db = Database()

    def get_all_anggota(self):
        conn = self.db.get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM anggota")
            return cursor.fetchall()
        except Error as e:
            print(f"Gagal mengambil data anggota: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def create_anggota(self, nama, alamat):
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            query = "INSERT INTO anggota (nama, alamat) VALUES (%s, %s)"
            cursor.execute(query, (nama, alamat))
            conn.commit()
            return True
        except Error as e:
            conn.rollback()
            print(f"Gagal menambah anggota: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def update_anggota(self, id_anggota, nama, alamat):
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            query = "UPDATE anggota SET nama=%s, alamat=%s WHERE id_anggota=%s"
            cursor.execute(query, (nama, alamat, id_anggota))
            conn.commit()
            return True
        except Error as e:
            conn.rollback()
            print(f"Gagal mengubah anggota: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def delete_anggota(self, id_anggota):
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            query = "DELETE FROM anggota WHERE id_anggota=%s"
            cursor.execute(query, (id_anggota,))
            conn.commit()
            return True
        except Error as e:
            conn.rollback()
            print(f"Gagal menghapus anggota: {e}")
            return False
        finally:
            cursor.close()
            conn.close()