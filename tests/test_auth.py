import hashlib
from unittest.mock import MagicMock, patch
from models.user_model import UserModel
from controllers.auth_controller import AuthController

def test_hash_password_sha256():
    user_model = UserModel()
    hasil_hash = user_model.hash_password("admin123")
    expected_hash = hashlib.sha256("admin123".encode("utf-8")).hexdigest()

    assert hasil_hash == expected_hash
    assert len(hasil_hash) == 64

def test_verify_user_berhasil():
    user_model = UserModel()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {
        "id_user": 1,
        "username": "petugas",
        "role": "admin"
    }

    user_model.db.get_connection = MagicMock(return_value=mock_conn)
    hasil = user_model.verify_user("petugas", "admin123")

    assert hasil is not None
    assert hasil["username"] == "petugas"
    assert hasil["role"] == "admin"

@patch("controllers.auth_controller.BukuController")
def test_login_controller_berhasil(mock_buku_controller):
    mock_model = MagicMock()
    mock_view = MagicMock()
    mock_view.get_credentials.return_value = ("petugas", "admin123")
    mock_model.verify_user.return_value = {
        "id_user": 1,
        "username": "petugas",
        "role": "admin"
    }

    controller = AuthController(model=mock_model, view=mock_view)
    controller.proses_login()

    mock_view.show_info.assert_called_once()
    mock_view.destroy.assert_called_once()
    mock_buku_controller.assert_called_once_with(user_role="admin")

def test_login_controller_gagal():
    mock_model = MagicMock()
    mock_view = MagicMock()
    mock_view.get_credentials.return_value = ("petugas", "salahpassword")
    mock_model.verify_user.return_value = None

    controller = AuthController(model=mock_model, view=mock_view)
    controller.proses_login()

    mock_view.show_error.assert_called_once_with("Username atau password salah!")