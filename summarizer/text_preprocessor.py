from logger.logger import get_logger

logger = get_logger(__name__)

def preprocess_text(text):
    try:
        return text.replace('\n', ' ').strip()
    except Exception as e:
        logger.error(f"Failed to preprocess text: {str(e)}")
        raise
