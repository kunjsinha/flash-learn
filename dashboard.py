import streamlit as st

# Page config
st.set_page_config(page_title="Flash Learn", page_icon="📚", layout="centered")

# Add some spacing from top
st.markdown("<br>", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>Welcome User</h1>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Navigation buttons - centered with better spacing
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("📚 Flashcard App", type="primary", use_container_width=True):
        st.switch_page("pages/flashcard_ui.py")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("⌨️ Typing Test", type="primary", use_container_width=True):
        st.switch_page("pages/typing_test.py")
