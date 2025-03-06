# utils/file_utils.py
from io import BytesIO
import pdfplumber
import docx

def handle_file_upload(uploaded_file) -> str:
    """
    Convert an uploaded file to text.
    Supports PDF, DOCX, and TXT files.
    """
    if uploaded_file is None:
        raise ValueError("No file uploaded!")
    
    content_bytes = uploaded_file.read()
    
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(content_bytes)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(content_bytes)
    else:
        try:
            return content_bytes.decode("utf-8")
        except UnicodeDecodeError:
            return content_bytes.decode("ISO-8859-1", errors="replace")

def extract_text_from_pdf(content_bytes: bytes) -> str:
    with pdfplumber.open(BytesIO(content_bytes)) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def extract_text_from_docx(content_bytes: bytes) -> str:
    doc = docx.Document(BytesIO(content_bytes))
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text.strip()
