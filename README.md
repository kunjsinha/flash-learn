# AI Flashcard Generator 

Currently only ai.py file exists which is the brain of the app.

## Prerequisites

1.  **Python 3.x**: Ensure you have Python installed.
2.  **Ollama**: You need to have [Ollama](https://ollama.com/) installed and running on your machine.
3.  **Model**: The script defaults to using `llama3.2:1b`. You need to pull this model (or the one you intend to use).
4.  **Python Libraries**: The script requires the `requests` library.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install requests
    ```

2.  **Pull the Model**:
    Make sure Ollama is running, then pull the model specified in the script (default is `llama3.2:1b`):
    ```bash
    ollama pull llama3.2:1b
    ```

## Usage

To test the generator with the built-in sample text, simply run the script directly:

```bash
python ai.py
```

This will:
1.  Initialize the `LocalQuestionGenerator`.
2.  Send a sample text about CPUs to the local Ollama instance.
3.  Print the generated JSON containing the questions.

## Customization

You can modify the `if __name__ == "__main__":` block in `ai.py` to:
-   Change the `model_name` passed to `LocalQuestionGenerator`.
-   Update `sample_text` with your own content.
-   Adjust parameters like `count` (number of questions), `difficulty`, or `q_type` in the `generate_questions` call.
