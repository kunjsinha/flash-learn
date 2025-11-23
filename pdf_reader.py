import os
import fitz  # PyMuPDF
import re

# extract text from pdf and cleanup to return JSON formatted string

def extract_text_from_pdf(pdf_path: str) -> str:

    if not os.path.exists(pdf_path):
        return f"Error: The file '{pdf_path}' was not found."
    
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def clean_json_response(response: str) -> str:
    cleaned = response.strip()
    
    # Remove markdown code blocks
    if cleaned.startswith("```"):
        lines = cleaned.split('\n')
        lines = lines[1:]  # Remove first line
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        cleaned = '\n'.join(lines).strip()
    
    # Find the JSON array if there's extra text
    if not cleaned.startswith('['):
        start_idx = cleaned.find('[')
        if start_idx != -1:
            cleaned = cleaned[start_idx:]
    
    # Remove trailing commas before closing brackets/braces
    cleaned = re.sub(r',(\s*[}\]])', r'\1', cleaned)
    
    # Fix missing closing bracket - LLM often forgets the final ] and }
    if cleaned.startswith('[') and not cleaned.rstrip().endswith(']'):
        open_count = cleaned.count('[')
        close_count = cleaned.count(']')
        open_curly_brace_count = cleaned.count('{')
        close_curly_brace_count = cleaned.count('}')
        if open_curly_brace_count > close_curly_brace_count:
            cleaned = cleaned.rstrip() + '}'
        if open_count > close_count:
            cleaned = cleaned.rstrip() + ']'
    
    return cleaned

if __name__ == "__main__":
    print("Testing pdf_reader.py capabilities") # testing some sample files
    pdf_path = input("Enter the path to the PDF file: ").strip()
    # Clean up file directory string
    if pdf_path.startswith('"') and pdf_path.endswith('"'):
        pdf_path = pdf_path[1:-1]
    elif pdf_path.startswith("'") and pdf_path.endswith("'"):
        pdf_path = pdf_path[1:-1]
        
    extracted_text = extract_text_from_pdf(pdf_path)
    print("\n--- Extracted Text ---\n")
    print(extracted_text)
