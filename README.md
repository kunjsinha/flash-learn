# 📚 Flash Learn

A study tool with user authentication, AI-powered flashcards, and a typing speed test.
This was done for a university mini project.

## Features

- **User Authentication**: Secure login/signup system with Google Sheets backend
- **Flashcard App**: Upload PDFs and generate AI-powered study questions
- **Typing Test**: Test your typing speed with real-time feedback

## Prerequisites

1. **Python 3.8+**
2. **Ollama** - [Download here](https://ollama.com/)
3. **Google Cloud Account** - For authentication backend

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kunjsinha/flash-learn.git
   cd flash-learn
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pymupdf requests gspread google-auth
   ```

3. **Setup Ollama**
   ```bash
   ollama pull llama3.2
   ```

4. **Setup Google Sheets Authentication**
   
   a. Create a Google Cloud Project and enable Google Sheets API
   
   b. Create a Service Account and download the JSON credentials
   
   c. Create a Google Sheet named "users" with columns: `username` | `password`
   
   d. Share the sheet with your service account email
   
   e. Create `.streamlit/secrets.toml` with your credentials:
   ```toml
   [google]
   type = "service_account"
   project_id = "your-project-id"
   private_key_id = "your-private-key-id"
   private_key = "your-private-key"
   client_email = "your-service-account-email"
   client_id = "your-client-id"
   auth_uri = "https://accounts.google.com/o/oauth2/auth"
   token_uri = "https://oauth2.googleapis.com/token"
   auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
   client_x509_cert_url = "your-cert-url"
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

4. **Login or Sign Up** to access the dashboard

## Project Structure

- `app.py` - Application launcher
- `loginui.py` - Login/signup page
- `dashboard.py` - Main dashboard (protected)
- `pages/flashcard_ui.py` - Flashcard generator (protected)
- `pages/typing_test.py` - Typing speed test (protected)
- `ai.py` - AI question generation
- `pdf_reader.py` - PDF text extraction
- `wordgetter.py` - Word list utilities
- `wordsdataset.txt` - Word list for typing test
- `.streamlit/secrets.toml` - Google Cloud credentials (not in repo)

## Security Notes

- Keep `.streamlit/secrets.toml` private and never commit it to version control
- The Google Sheet should only be shared with your service account
