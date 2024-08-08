# summarizer/main.py

from summarizer.docx_reader import read_docx
from summarizer.text_preprocessor import preprocess_text
from summarizer.text_summarizer import summarize_long_text
from logger.logger import get_logger
from config.configuration import summary_length as default_summary_length

logger = get_logger(__name__)

def main(docx_file_path, summary_length=default_summary_length):
    logger.info("Reading DOCX file...")
    text = read_docx(docx_file_path)
    
    logger.info("Preprocessing text...")
    preprocessed_text = preprocess_text(text)
    
    logger.info("Summarizing text...")
    summary = summarize_long_text(preprocessed_text, summary_length)
    
    logger.info("Summary completed.")
    return summary
