from transformers import AutoTokenizer
from config.configuration import model_ckpt
from logger.logger import get_logger

logger = get_logger(__name__)

tokenizer = AutoTokenizer.from_pretrained(model_ckpt)

def split_text(text, max_length):
    try:
        tokens = tokenizer.encode(text, return_tensors='pt')[0]
        chunks = [tokens[i:i+max_length] for i in range(0, len(tokens), max_length)]
        return chunks
    except Exception as e:
        logger.error(f"Failed to split text: {str(e)}")
        raise
