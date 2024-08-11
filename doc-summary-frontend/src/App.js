import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Import CSS for styles

function App() {
  const [file, setFile] = useState(null);
  const [summaryLength, setSummaryLength] = useState(100);
  const [summary, setSummary] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSummaryLengthChange = (event) => {
    setSummaryLength(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setSummary('');
    setLoading(true);

    if (!file) {
      setError('Please upload a file.');
      setLoading(false);
      return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('summary_length', summaryLength);

    try {
      const response = await axios.post('/summarize/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.status === 200) {
        const { summary } = response.data;
        if (summary) {
          setSummary(summary);
        } else {
          setError('Summary is empty.');
        }
      } else {
        setError('Failed to summarize the document.');
      }
    } catch (error) {
      console.error('Error details:', error);
      setError('An error occurred while summarizing the document.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Document Summarizer</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="file">Upload Document:</label>
          <input
            type="file"
            id="file"
            name="file"
            accept=".docx"
            onChange={handleFileChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="summaryLength">Summary Length:</label>
          <input
            type="number"
            id="summaryLength"
            name="summary_length"
            value={summaryLength}
            onChange={handleSummaryLengthChange}
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Summarizing...' : 'Summarize'}
        </button>
      </form>
      {loading && <div className="spinner"></div>}
      {error && <p className="error-message">{error}</p>}
      {summary && (
        <div className="summary-container">
          <h2>Summary</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;
