from unittest.mock import MagicMock
from controllers.buku_controller import BukuController

def test_simpan_buku_berhasil():
    # Arrange
    mock_model = MagicMock()
    mock_view = MagicMock()
    mock_model.create_buku.return_value = True
    mock_model.get_all_buku.return_value = []
    mock_view.get_input_data.return_value = ("Clean Code", "Robert C. Martin", "2008")

    controller = BukuController(model=mock_model, view=mock_view)

    # Act
    controller.simpan_buku()

    # Assert
    mock_model.create_buku.assert_called_once_with("Clean Code", "Robert C. Martin", "2008")
    mock_view.show_info.assert_called_once_with("Data buku berhasil disimpan!")
    mock_view.clear_input.assert_called_once()

def test_simpan_buku_input_kosong():
    # Arrange
    mock_model = MagicMock()
    mock_view = MagicMock()
    mock_model.get_all_buku.return_value = []
    mock_view.get_input_data.return_value = ("", "Penulis", "2024")

    controller = BukuController(model=mock_model, view=mock_view)

    # Act
    controller.simpan_buku()

    # Assert
    mock_model.create_buku.assert_not_called()
    mock_view.show_error.assert_called_once_with("Semua kolom harus diisi!")

def test_get_all_buku():
    # Arrange
    mock_model = MagicMock()
    mock_view = MagicMock()
    data_dummy = [
        {"id_buku": 1, "judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun_terbit": 2005},
        {"id_buku": 2, "judul": "Bumi Manusia", "penulis": "Pramoedya Ananta Toer", "tahun_terbit": 1980},
    ]
    mock_model.get_all_buku.return_value = data_dummy

    # Act
    controller = BukuController(model=mock_model, view=mock_view)

    # Assert
    mock_model.get_all_buku.assert_called_once()
    mock_view.tampilkan_data.assert_called_once_with(data_dummy)