# summarizer/text_splitter.py

from transformers import AutoTokenizer
from config.configuration import model_ckpt

tokenizer = AutoTokenizer.from_pretrained(model_ckpt)

def split_text(text, max_length):
    tokens = tokenizer.encode(text, return_tensors='pt')[0]
    chunks = [tokens[i:i+max_length] for i in range(0, len(tokens), max_length)]
    return chunks
