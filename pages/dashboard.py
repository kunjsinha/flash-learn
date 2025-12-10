import streamlit as st

# Page config
st.set_page_config(page_title="Flash Learn", page_icon="📚", layout="centered")

# Initialize authentication state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None

# Redirect to login if not authenticated
if not st.session_state.authenticated:
    st.switch_page("loginui.py")

# Add some spacing from top
st.markdown("<br>", unsafe_allow_html=True)

# Title with personalized greeting
username = st.session_state.username or "User"
st.markdown(f"<h1 style='text-align: center;'>Welcome {username}</h1>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Navigation buttons - centered with better spacing
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("📚 Flashcard App", type="primary", use_container_width=True):
        st.switch_page("pages/flashcard_ui.py")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("⌨️ Typing Test", type="primary", use_container_width=True):
        st.switch_page("pages/typing_test.py")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Logout button
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.switch_page("loginui.py")
