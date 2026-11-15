import hashlib
from config.database import Database
from mysql.connector import Error

class UserModel:
    def __init__(self):
        self.db = Database()

    def hash_password(self, password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def register_user(self, username, password, role="anggota"):
        conn = self.db.get_connection()
        if not conn:
            return False
        try:
            hashed_pw = self.hash_password(password)
            cursor = conn.cursor()
            query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, hashed_pw, role))
            conn.commit()
            return True
        except Error as e:
            conn.rollback()
            print(f"Gagal mendaftarkan pengguna: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def verify_user(self, username, password):
        conn = self.db.get_connection()
        if not conn:
            return None
        try:
            hashed_pw = self.hash_password(password)
            cursor = conn.cursor(dictionary=True)
            query = "SELECT id_user, username, role FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, hashed_pw))
            return cursor.fetchone()
        except Error as e:
            print(f"Gagal memverifikasi pengguna: {e}")
            return None
        finally:
            cursor.close()
            conn.close()