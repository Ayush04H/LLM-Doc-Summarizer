import pytest
from pathlib import Path
import os
import sys

# Adding the path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from summarizer.docx_reader import read_docx
from summarizer.text_preprocessor import preprocess_text
from summarizer.text_summarizer import summarize_long_text
from config.configuration import summary_length as default_summary_length

# Path to the test document
docx_file_path = r'D:\placements2025\document_summary_app\backend\demo.docx'

@pytest.fixture
def single_summary():
    try:
        text = read_docx(docx_file_path)
        return text
    except Exception as e:
        pytest.fail(f"Failed to setup fixture: {str(e)}")

def test_summary_not_none(single_summary):
    """ Test that the summary is not None """
    assert single_summary is not None

def test_summary_str_type(single_summary):
    """ Test that the summary is of type str """
    assert isinstance(single_summary, str)

def test_summary_length(single_summary):
    """ Test that the summary length is within acceptable range """
    summary = summarize_long_text(single_summary, default_summary_length)
    word_count = len(summary.split())
    assert word_count <= (default_summary_length + 100)
    assert word_count >= (default_summary_length - 100)

def test_summary_not_empty(single_summary):
    """ Test that the summary is not empty """
    summary = summarize_long_text(single_summary, default_summary_length)
    assert len(summary.strip()) > 0

def test_summary_contains_keywords(single_summary):
    """ Test that the summary contains specific keywords """
    keywords = ['important', 'summary', 'document']
    summary = summarize_long_text(single_summary, default_summary_length)
    assert any(keyword in summary.lower() for keyword in keywords)

def test_summary_length_boundary_conditions(single_summary):
    """ Test boundary conditions for summary length """
    summary = summarize_long_text(single_summary, default_summary_length)
    word_count = len(summary.split())
    assert word_count == default_summary_length or word_count == default_summary_length + 100 or word_count == default_summary_length - 100

def test_large_document():
    """ Test handling of large document """
    large_docx_file_path = r'D:\placements2025\document_summary_app\backend\large_document.docx'
    try:
        text = read_docx(large_docx_file_path)
        summary = summarize_long_text(text, default_summary_length)
        assert summary is not None
    except Exception as e:
        pytest.fail(f"Failed in test_large_document: {str(e)}")

def test_empty_document():
    """ Test behavior with an empty document """
    empty_docx_file_path = r'D:\placements2025\document_summary_app\backend\empty_document.docx'
    try:
        text = read_docx(empty_docx_file_path)
        summary = summarize_long_text(text, default_summary_length)
        assert summary == ""
    except Exception as e:
        pytest.fail(f"Failed in test_empty_document: {str(e)}")

def test_invalid_docx_file():
    """ Test handling of invalid DOCX file """
    invalid_docx_file_path = r'D:\placements2025\document_summary_app\backend\invalid_document.docx'
    try:
        text = read_docx(invalid_docx_file_path)
        pytest.fail("Expected exception for invalid DOCX file was not raised")
    except Exception:
        pass  # Expected behavior
