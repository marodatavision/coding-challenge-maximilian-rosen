import pytest
from unittest.mock import patch
from app.services import document_loader

@pytest.fixture(autouse=True)
def reset_settings(monkeypatch):
    # Setzt Einstellungen jedes Mal neu
    monkeypatch.setenv("USE_GDRIVE", "false")
    monkeypatch.setenv("GDRIVE_FOLDER_ID", "")
    yield

@patch("app.services.local_pdf_loader.load_local_documents")
def test_load_local_documents_called(mock_local_loader, monkeypatch):
    monkeypatch.setenv("USE_GDRIVE", "false")

    mock_local_loader.return_value = ["DUMMY_LOCAL_DOC"]

    docs = document_loader.load_documents()

    mock_local_loader.assert_called_once()
    assert docs == ["DUMMY_LOCAL_DOC"]

@patch("app.services.gdrive_loader.load_gdrive_documents")
def test_load_gdrive_documents_called(mock_gdrive_loader, monkeypatch):
    monkeypatch.setenv("USE_GDRIVE", "true")
    monkeypatch.setenv("GDRIVE_FOLDER_ID", "abc123")

    mock_gdrive_loader.return_value = ["DUMMY_GDRIVE_DOC"]

    docs = document_loader.load_documents()

    mock_gdrive_loader.assert_called_once_with(folder_id="abc123")
    assert docs == ["DUMMY_GDRIVE_DOC"]
