# utils/file_converter.py

from fpdf import FPDF
from docx import Document
from io import BytesIO

def generate_pdf(resume_text: str) -> BytesIO:
    """
    Convert the resume text into a PDF file.
    Returns a BytesIO object containing the PDF.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add each line of the resume text into the PDF.
    for line in resume_text.split("\n"):
        pdf.multi_cell(0, 10, txt=line)
    
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)  # Reset the pointer to the beginning.
    return pdf_output

def generate_docx(resume_text: str) -> BytesIO:
    """
    Convert the resume text into a DOCX file.
    Returns a BytesIO object containing the DOCX.
    """
    document = Document()
    
    # Add each line as a separate paragraph.
    for line in resume_text.split("\n"):
        document.add_paragraph(line)
    
    docx_output = BytesIO()
    document.save(docx_output)
    docx_output.seek(0)
    return docx_output
