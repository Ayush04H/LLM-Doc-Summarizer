import docx
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load the pre-trained model and tokenizer
model_ckpt = 'facebook/bart-large-cnn'
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)

# Move the model to GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

def read_docx(file_path):
    """
    Reads the text from a DOCX file.
    """
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def preprocess_text(text):
    """
    Preprocess the text to improve summarization quality.
    """
    return text.replace('\n', ' ').strip()

def split_text(text, max_length):
    """
    Splits the text into smaller chunks to fit the model's maximum length.
    """
    tokens = tokenizer.encode(text, return_tensors='pt')[0]
    chunks = [tokens[i:i+max_length] for i in range(0, len(tokens), max_length)]
    return chunks

def summarize_text(text, summary_length):
    """
    Summarizes the input text using the BART model.
    """
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True).to(device)
    
    summary_ids = model.generate(
        inputs, 
        max_length=summary_length, 
        min_length=int(summary_length * 0.5), 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True,
        do_sample=True,  # Enable sampling
        temperature=0.7,  # Control the randomness of predictions
        top_k=50,         # Limit the sampling pool to the top-k tokens
        top_p=0.95        # Nucleus sampling
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def summarize_long_text(text, summary_length):
    """
    Handles long text by splitting it into chunks, summarizing each chunk, and combining the results.
    """
    chunks = split_text(text, 1024)  # Use a suitable chunk size
    summaries = []
    for chunk in chunks:
        chunk_text = tokenizer.decode(chunk, skip_special_tokens=True)
        chunk_summary = summarize_text(chunk_text, summary_length)
        summaries.append(chunk_summary)
    combined_summary = " ".join(summaries)
    return combined_summary

def main(docx_file_path, summary_length):
    """
    Main function to summarize a DOCX document.
    """
    text = read_docx(docx_file_path)
    preprocessed_text = preprocess_text(text)
    summary = summarize_long_text(preprocessed_text, summary_length)
    print("Summary:")
    print(summary)

if __name__ == "__main__":
    # Path to the DOCX file
    docx_file_path = r'D:\placements2025\document_summary_app\demo.docx'
    
    # Set the desired summary length
    summary_length = 200  # You can change this value as needed
    
    main(docx_file_path, summary_length)
