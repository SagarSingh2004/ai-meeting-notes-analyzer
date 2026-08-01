from docx import Document
from pypdf import PdfReader


def read_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")


def read_docx(uploaded_file):
    doc = Document(uploaded_file)

    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return "\n".join(text)


def read_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)

    text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text)