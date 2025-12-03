# 📚 Flash Learn

A simple study tool with AI-powered flashcards and a typing speed test.

## Features

- **📚 Flashcard App**: Upload PDFs and generate AI-powered study questions
- **⌨️ Typing Test**: Test your typing speed with real-time feedback

## Prerequisites

1. **Python 3.8+**
2. **Ollama** - [Download here](https://ollama.com/)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kunjsinha/flash-learn.git
   cd flash-learn
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pymupdf requests
   ```

3. **Setup Ollama**
   ```bash
   ollama pull llama3.2
   ```

## Usage

1. **Start Ollama** (if not already running)
   ```bash
   ollama serve
   ```

2. **Run the app**
   ```bash
   python app.py
   ```

3. **Open your browser** to `http://localhost:8501`

## Project Structure

- `app.py` - Application launcher
- `dashboard.py` - Main dashboard
- `pages/flashcard_ui.py` - Flashcard generator
- `pages/typing_test.py` - Typing speed test
- `ai.py` - AI question generation
- `pdf_reader.py` - PDF text extraction
- `wordgetter.py` - Word list utilities
- `wordsdataset.txt` - Word list
- `README.md` - Project documentation
