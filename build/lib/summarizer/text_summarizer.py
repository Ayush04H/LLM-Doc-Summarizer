from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from config.configuration import model_ckpt, temperature, top_k, top_p, summary_length
from logger.logger import get_logger

logger = get_logger(__name__)

tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

def summarize_text(text, summary_length):
    try:
        inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True).to(device)
        
        summary_ids = model.generate(
            inputs, 
            max_length=summary_length, 
            min_length=int(summary_length * 0.8), 
            length_penalty=2.0, 
            num_beams=4, 
            early_stopping=True,
            do_sample=True,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        # Ensure summary length is within the acceptable range
        word_count = len(summary.split())
        if abs(word_count - summary_length) > 100:
            logger.warning(f"Summary length of {word_count} words is outside the acceptable range. Adjusting...")
            adjusted_length = max(100, min(summary_length + (summary_length - word_count), summary_length + 100))
            summary_ids = model.generate(
                inputs, 
                max_length=adjusted_length, 
                min_length=int(adjusted_length * 0.8), 
                length_penalty=2.0, 
                num_beams=4, 
                early_stopping=True,
                do_sample=True,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p
            )
            summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary
    
    except Exception as e:
        logger.error(f"Failed to summarize text: {str(e)}")
        raise

def summarize_long_text(text, summary_length):
    from summarizer.text_splitter import split_text
    try:
        chunks = split_text(text, 1024)
        summaries = []
        for chunk in chunks:
            chunk_text = tokenizer.decode(chunk, skip_special_tokens=True)
            chunk_summary = summarize_text(chunk_text, summary_length)
            summaries.append(chunk_summary)
        combined_summary = " ".join(summaries)
        
        # Further adjust if combined summary is too long
        combined_word_count = len(combined_summary.split())
        if combined_word_count > summary_length + 100:
            combined_summary = " ".join(combined_summary.split()[:summary_length])

        return combined_summary
    
    except Exception as e:
        logger.error(f"Failed to summarize long text: {str(e)}")
        raise
