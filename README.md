# LLM-Doc-Summarizer

LLM-Doc-Summarizer is a web application designed to simplify the process of summarizing lengthy documents using advanced natural language processing (NLP) techniques. Leveraging the power of the `facebook/bart-large-cnn` model, this application provides users with concise and accurate summaries of uploaded documents, making it easier to digest and understand large volumes of text.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Document Upload**: Users can upload `.docx` files for summarization.
- **Customizable Summary Length**: Users can specify the desired length of the summary, tailoring the output to their needs.
- **Real-time Summarization**: Summaries are generated instantly after the document is uploaded, ensuring quick turnaround.
- **User-friendly Interface**: The frontend is simple and intuitive, allowing users to easily interact with the application.

## Technologies Used
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **Frontend**: [React](https://reactjs.org/) - A JavaScript library for building user interfaces.
- **Model**: [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) - A pre-trained NLP model designed for text summarization.
- **Server**: [Uvicorn](https://www.uvicorn.org/) - A lightning-fast ASGI server implementation, using [uvloop](https://github.com/MagicStack/uvloop) and [httptools](https://github.com/MagicStack/httptools).

## Installation

### Prerequisites
- Python 3.7+
- Node.js 14+
- npm or yarn

### Clone the Repository
```bash
git clone https://github.com/Ayush04H/LLM-Doc-Summarizer.git
cd LLM-Doc-Summarizer
