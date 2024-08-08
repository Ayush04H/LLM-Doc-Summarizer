# run_summary.py

from summarizer.main import main
import config.configuration as config

if __name__ == "__main__":
    # Path to the DOCX file
    docx_file_path = config.docx_file_path
    
    # Run the summarization process
    summary = main(docx_file_path, config.summary_length)
    print("Summary:")
    print(summary)
