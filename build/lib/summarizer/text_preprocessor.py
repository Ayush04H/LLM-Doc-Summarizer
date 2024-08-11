# summarizer/text_preprocessor.py

from logger.logger import get_logger

logger = get_logger(__name__)

def preprocess_text(text):
    try:
        text = text.replace('\n', ' ').replace('\r', '').strip()
        text = ' '.join(text.split())  # Remove excessive spaces
        return text
    except Exception as e:
        logger.error(f"Failed to preprocess text: {str(e)}")
        raise
