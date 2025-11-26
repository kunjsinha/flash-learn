import subprocess
import sys

def run_streamlit():
    subprocess.Popen([
        sys.executable,
        "-m", "streamlit",
        "run",
        "ui/main_ui.py"
    ])

if __name__ == "__main__":
    run_streamlit()

# pkill -f streamlit to kill streamlit process on mac
