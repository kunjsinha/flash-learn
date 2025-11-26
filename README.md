# 📚 Flash Learn

**Flash Learn** is an AI-powered study assistant that turns your PDF documents into interactive flashcards and quizzes. Built with Streamlit and powered by local LLMs via Ollama, it helps you study more efficiently by automatically generating questions from your reading materials.

## ✨ Features

-   **📄 PDF Text Extraction**: Upload any PDF document to extract its content.
-   **🤖 AI Question Generation**: Uses a local Ollama model (default: `llama3.2`) to generate high-quality Multiple Choice Questions (MCQs).
-   **🎴 Flashcard Mode**: Study questions one by one with an interactive "reveal answer" feature.
-   **📋 List View**: Review all generated questions, answers, and explanations in a structured list.
-   **🔒 Privacy Focused**: Runs entirely locally on your machine using Ollama—no data leaves your computer.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2.  **Ollama**: [Download Ollama](https://ollama.com/)
3.  **Ollama Model**: You need to pull the Llama 3.2 model (or your preferred model).

## 🚀 Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/kunjsinha/flash-learn.git
    cd flash-learn
    ```

2.  **Install Python Dependencies**
    ```bash
    pip install streamlit pymupdf requests
    ```

3.  **Setup Ollama**
    Make sure Ollama is installed and running, then pull the required model:
    ```bash
    ollama pull llama3.2
    ```
    *Note: You can use other models (like `llama3.2:1b` for faster performance on lower-end hardware) by modifying the `model_name` in `ui/main_ui.py`.*

## 🎮 Usage

1.  **Start the Ollama Server**
    Ensure Ollama is running in the background:
    ```bash
    ollama serve
    ```

2.  **Run the Application**
    Launch the Streamlit app using the provided wrapper script:
    ```bash
    python app.py
    ```
    *Alternatively, you can run it directly with Streamlit:*
    ```bash
    streamlit run ui/main_ui.py
    ```

3.  **Generate Flashcards**
    -   Open the URL provided in the terminal (usually `http://localhost:8501`).
    -   **Upload** your PDF file.
    -   Click **"Generate Questions"**.
    -   Wait for the AI to process the text and create questions.
    -   Switch between **"View All Questions"** and **"Start Flashcards"** modes to study!

## 📂 Project Structure

-   `app.py`: Entry point script to launch the application.
-   `ui/main_ui.py`: The main Streamlit user interface and application logic.
-   `ai.py`: Handles interactions with the local Ollama API for question generation.
-   `pdf_reader.py`: Utilities for extracting and cleaning text from PDF files.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.
