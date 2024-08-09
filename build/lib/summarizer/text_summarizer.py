# summarizer/text_summarizer.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from config.configuration import model_ckpt, temperature, top_k, top_p, summary_length

tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

def summarize_text(text, summary_length):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True).to(device)
    
    summary_ids = model.generate(
        inputs, 
        max_length=summary_length, 
        min_length=int(summary_length * 0.5), 
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

def summarize_long_text(text, summary_length):
    from summarizer.text_splitter import split_text
    chunks = split_text(text, 1024)
    summaries = []
    for chunk in chunks:
        chunk_text = tokenizer.decode(chunk, skip_special_tokens=True)
        chunk_summary = summarize_text(chunk_text, summary_length)
        summaries.append(chunk_summary)
    combined_summary = " ".join(summaries)
    return combined_summary