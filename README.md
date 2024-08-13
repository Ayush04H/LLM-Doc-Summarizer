
# LLM-Doc-Summarizer

LLM-Doc-Summarizer is a document summarization application that leverages the power of the `facebook/bart-large-cnn` model. The project provides a web-based interface where users can upload `.docx` files and receive concise summaries based on a specified summary length. The backend is built with FastAPI, while the frontend is created using React.

## Features

- **Document Upload**: Users can upload `.docx` files to the application.
- **Customizable Summary Length**: Users can specify the desired length of the summary.
- **Real-time Summarization**: The app provides a summary in real-time after processing the uploaded document.
- **Error Handling**: Graceful error handling ensures that users are notified of any issues during the summarization process.

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js and npm

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ayush04H/LLM-Doc-Summarizer.git
   cd LLM-Doc-Summarizer
   ```

2. **Backend Setup**

   Navigate to the backend directory and create a virtual environment:

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Frontend Setup**

   Navigate to the frontend directory and install the dependencies:

   ```bash
   cd ../doc-summary-frontend
   npm install
   ```

### Running the Application

1. **Run the Backend**

   Navigate to the backend directory and start the FastAPI server:

   ```bash
   cd backend
   uvicorn app:app --reload
   ```

   The backend server will run on `http://127.0.0.1:8000`.

2. **Run the Frontend**

   Navigate to the frontend directory and start the React development server:

   ```bash
   cd ../doc-summary-frontend
   npm start
   ```

   The frontend will run on `http://localhost:3000`.

### Usage

1. Open the application in your web browser at `http://localhost:3000`.
2. Upload a `.docx` file using the provided form.
3. Specify the desired summary length.
4. Click the "Summarize" button.
5. View the generated summary on the page.

### Project Structure

- **backend/**: Contains the FastAPI backend application.
  - **summarizer/**: Contains the core summarization logic.
  - **config/**: Configuration files for the application.
  - **app.py**: Main entry point for the FastAPI server.
  
- **doc-summary-frontend/**: Contains the React frontend application.
  - **src/**: Source code for the frontend, including components and styles.
  - **public/**: Public assets and HTML files.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

### Commands to Clone and Fork the Repository

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ayush04H/LLM-Doc-Summarizer.git
   ```

2. **Fork the Repository**

   Visit the repository on GitHub and click on the "Fork" button on the top right to create your own copy.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries or further information, please feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/ayush-srivastava-aks04102002/).
