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