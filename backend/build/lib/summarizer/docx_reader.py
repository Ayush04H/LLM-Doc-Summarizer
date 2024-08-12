# summarizer/docx_reader.py

import docx
from logger.logger import get_logger

logger = get_logger(__name__)

def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        logger.error(f"Failed to read DOCX file at {file_path}: {str(e)}")
        raise
