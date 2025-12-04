import requests


class LocalQuestionGenerator:
    def __init__(self, model_name: str = "llama3.2"):
        # initialize local model via ollama
        self.model_name = model_name
        self.url = "http://localhost:11434/api/generate"
        print(f"--- Agent Initialized with Local Model: {model_name} ---")

    def generate_questions(self, text_content: str, q_type: str = "mcq", count: int = 5, difficulty: str = "hard") -> str:

        prompt = f"""
        You are an expert academic examiner. Generate high-quality assessment questions based ONLY on the provided text.
        
        CONTEXT:
        {text_content}

        INSTRUCTIONS:
        - Generate {count} {difficulty} questions.
        - Question type: {q_type.upper()}.
        - Output MUST be valid JSON.
        - The questions should be split across multiple topics from the text.
        - There should be a clear explanation for each question.
        - Use this format exactly:
        IMPORTANT: 
        - DO NOT use LaTeX.
        - Do not mess up te JSON string format and remember to close "".
        - ANY MATH MARKUP IS NOT ALLOWED.
        - DO NOT use math symbols.
        - DO NOT use unicode symbols.
        - ALL OUTPUT MUST BE IN PLAIN TEXT AND NUMBERS ONLY.
        - DO NOT use any special characters.

        [
            {{
                "type": "mcq",
                "question": "...",
                "options": ["A...", "B...", "C...", "D..."],
                "correct_answer": "Option text",
                "explanation": "Provide a good explanation in one sentence mostly"
            }}
        ]
        
        Only use this format do not forget any part of the json format.
        
        ONLY output the JSON. No notes, no commentary.
        AGAIN, DO NOT use LaTeX or any symbol markup.
        """

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False  # required for safe GUI usage
        }

        try:
            response = requests.post(self.url, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")

        except Exception as e:
            return f"Error: {e}\nMake sure Ollama is running and you have pulled the model (ollama pull {self.model_name})"


if __name__ == "__main__":
    print("Testing ai.py capabilities")
    sample_text = """
    The Central Processing Unit (CPU) is the primary component of a computer 
    that acts as its 'brain.' The CPU performs basic arithmetic, logic, 
    controlling, and input/output (I/O) operations specified by program instructions.
    """ # some sample text

    agent = LocalQuestionGenerator(model_name="llama3.2:1b")
    print("\n--- Generating Questions locally to test ai ---")
    result = agent.generate_questions(sample_text, q_type="mcq", count=10, difficulty="easy")
    print(result)
