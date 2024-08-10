# summarizer/text_splitter.py

from transformers import AutoTokenizer
from config.configuration import model_ckpt
from logger.logger import get_logger

logger = get_logger(__name__)

tokenizer = AutoTokenizer.from_pretrained(model_ckpt)

def split_text(text, max_length):
    try:
        tokens = tokenizer.encode(text, return_tensors='pt')[0]
        chunks = []
        start = 0
        while start < len(tokens):
            end = min(start + max_length, len(tokens))
            if end < len(tokens):
                while end > start and tokenizer.decode(tokens[end]) not in ['.', '!', '?']:
                    end -= 1
            chunk = tokens[start:end]
            chunks.append(chunk)
            start = end
        return chunks
    except Exception as e:
        logger.error(f"Failed to split text: {str(e)}")
        raise
