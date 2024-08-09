# logger/logger.py

import logging
import os

def get_logger(name, log_dir='D:\\placements2025\\document_summary_app\\logs', log_file='app.log'):
    """
    Set up a logger that writes to both the console and a file in the specified directory.
    
    :param name: Name of the logger.
    :param log_dir: Directory to store the log file.
    :param log_file: Name of the log file.
    :return: Configured logger instance.
    """
    # Ensure the log directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create console handler for outputting to the console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    # Create file handler for outputting to a log file in the specified directory
    file_path = os.path.join(log_dir, log_file)
    fh = logging.FileHandler(file_path)
    fh.setLevel(logging.DEBUG)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    
    return logger
