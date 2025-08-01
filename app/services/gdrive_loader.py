from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import tempfile
from app.core.models.document import Document

def load_gdrive_documents(folder_id: str) -> list[Document]:
    gauth = GoogleAuth()
    # Authentifiziere über Service-Account
    gauth.LoadServiceConfigFile(os.getenv("GDRIVE_SERVICE_ACCOUNT_FILE"))
    drive = GoogleDrive(gauth)

    file_list = drive.ListFile({
        'q': f"'{folder_id}' in parents and mimeType='application/pdf' and trashed=false"
    }).GetList()

    documents = []

    for file in file_list:
        print(f"📥 Lade: {file['title']}")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            file.GetContentFile(tmp_file.name)
            with open(tmp_file.name, "rb") as f:
                content = f.read()
            documents.append(Document(text=content.decode("latin1"), metadata={"source": file['title']}))
            os.unlink(tmp_file.name)

    return documents
