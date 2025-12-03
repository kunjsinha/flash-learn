import streamlit as st
import sys
import os
import json



# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pdf_reader import extract_text_from_pdf, clean_json_response
from ai import LocalQuestionGenerator

# Page config
st.set_page_config(page_title="Flash Learn - Flashcards", page_icon="📚", layout="wide")

# Back to Dashboard button
if st.button("⬅️ Back to Dashboard"):
    st.switch_page("dashboard.py")

# Title
st.title("📚 Flash Learn - Flashcard Generator")
st.markdown("---")

# Initialize session state
if 'ai_agent' not in st.session_state:
    st.session_state.ai_agent = None
if 'questions' not in st.session_state:
    st.session_state.questions = None
if 'flashcard_mode' not in st.session_state:
    st.session_state.flashcard_mode = False
if 'current_card' not in st.session_state:
    st.session_state.current_card = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=['pdf'])

# Generate button
if uploaded_file is not None:
    if st.button("Generate Questions", type="primary"):
        with st.spinner("Initializing AI and generating questions... Please wait."):
            try:
                # Save uploaded file temporarily
                temp_path = f"/tmp/{uploaded_file.name}"
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Initialize AI 
                if st.session_state.ai_agent is None:
                    st.session_state.ai_agent = LocalQuestionGenerator(model_name="llama3.2")
                
                # Extract text
                text = extract_text_from_pdf(temp_path)
                
                if text.startswith("Error"):
                    st.error(text)
                else:
                    # Generate questions
                    questions_json = st.session_state.ai_agent.generate_questions(
                        text, count=5, difficulty="hard", q_type="mcq"
                    )
                    
                    try:
                        # Clean the JSON response
                        cleaned_json = clean_json_response(questions_json)
                        
                        # If still empty or invalid, show the raw response
                        if not cleaned_json:
                            st.error("AI returned an empty response")
                            st.code(questions_json)
                        else:
                            st.session_state.questions = json.loads(cleaned_json)
                            st.session_state.flashcard_mode = False
                            st.session_state.current_card = 0
                            st.session_state.show_answer = False
                            st.success("Questions generated successfully!")
                    except json.JSONDecodeError as e:
                        st.error(f"Error parsing AI response: {str(e)}")
                        st.write("**Raw AI Response:**")
                        st.code(questions_json)
                        st.write("**Cleaned Response:**")
                        st.code(cleaned_json if 'cleaned_json' in locals() else "N/A")
                
                # Clean up temp file
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Display questions or flashcards
if st.session_state.questions:
    st.markdown("---")
    
    # Mode selection
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 View All Questions"):
            st.session_state.flashcard_mode = False
    with col2:
        if st.button("🎴 Start Flashcards"):
            st.session_state.flashcard_mode = True
            st.session_state.current_card = 0
            st.session_state.show_answer = False
    
    st.markdown("---")
    
    if st.session_state.flashcard_mode:
        # Flashcard mode
        total_cards = len(st.session_state.questions)
        current = st.session_state.current_card
        q = st.session_state.questions[current]
        
        # Progress
        st.progress((current + 1) / total_cards)
        st.caption(f"Card {current + 1} of {total_cards}")
        
        # Question card
        st.markdown(f"### {q.get('question', 'Unknown')}")
        
        # Options
        if "options" in q:
            st.markdown("**Options:**")
            for opt in q["options"]:
                st.markdown(f"- {opt}")
        
        st.markdown("")
        
        # Answer button
        if not st.session_state.show_answer:
            if st.button("🔍 Show Answer", key="show_answer_btn"):
                st.session_state.show_answer = True
                st.rerun()
        else:
            # Show answer
            st.success(f"**✓ Answer:** {q.get('correct_answer', 'N/A')}")
            st.info(f"**Explanation:** {q.get('explanation', '')}")
        
        # Navigation
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if current > 0:
                if st.button("⬅️ Previous"):
                    st.session_state.current_card -= 1
                    st.session_state.show_answer = False
                    st.rerun()
        
        with col3:
            if current < total_cards - 1:
                if st.button("Next ➡️"):
                    st.session_state.current_card += 1
                    st.session_state.show_answer = False
                    st.rerun()
            else:
                if st.button("🎉 Finish"):
                    st.session_state.flashcard_mode = False
                    st.balloons()
                    st.rerun()
    
    else:
        # List view mode
        st.subheader("Generated Questions")
        
        for i, q in enumerate(st.session_state.questions, 1):
            with st.expander(f"**Question {i}**: {q.get('question', 'Unknown')}", expanded=False):
                # Options
                if "options" in q:
                    st.markdown("**Options:**")
                    for opt in q["options"]:
                        st.markdown(f"- {opt}")
                
                # Answer
                st.markdown(f"**✓ Answer:** :green[{q.get('correct_answer', 'N/A')}]")
                
                # Explanation
                st.markdown(f"**Explanation:** _{q.get('explanation', '')}_")



    