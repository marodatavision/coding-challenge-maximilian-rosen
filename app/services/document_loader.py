from app.config import settings
from app.services.local_pdf_loader import load_local_documents
from app.services.gdrive_loader import load_gdrive_documents

def load_documents() -> list:
    if settings.use_gdrive:
        return load_gdrive_documents(folder_id=settings.gdrive_folder_id)
    else:
        return load_local_documents(path="data/pdfs")
