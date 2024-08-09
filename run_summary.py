from summarizer.main import main
import config.configuration as config
from logger.logger import get_logger

logger = get_logger(__name__)

if __name__ == "__main__":
    try:
        docx_file_path = config.docx_file_path
        
        # Run the summarization process
        summary = main(docx_file_path, config.summary_length)
        print("Summary:")
        print(summary)
    except Exception as e:
        logger.error(f"Failed to run summary: {str(e)}")
