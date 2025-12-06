import streamlit as st
import gspread #used to read and write to the google sheet
from google.oauth2.service_account import Credentials
import re

# Page config
st.set_page_config(page_title="Flash Learn - Login", page_icon="🔐", layout="centered")

# Initialize authentication state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None

# Redirect to dashboard if already authenticated
if st.session_state.authenticated:
    st.switch_page("dashboard.py")



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["google"],
    scopes=SCOPE
) #st.secrets reads the .secrets.toml file

client = gspread.authorize(creds)
sheet = client.open("users").sheet1 


col1,col2,col3=st.columns([1,3,1])#column width ratio to position the titles
st.subheader("_Hey! Welcome to_ :violet[Flash-Learn]",divider="gray")
with col2:
    st.title("FLASH-LEARN🗃️")
st.subheader("login/sign-up",divider="green")
col1,col2,col3,col4=st.columns([1,2,2,1]) #column width ratios to position buttons

#setting initial session_state for both forms to false   
if "show_login" not in st.session_state:
    st.session_state.show_login=False
if "show_signup" not in st.session_state:
    st.session_state.show_signup=False

#changing session_state when buttons are clicked
with col2:
    if st.button("🔐login"):
        st.session_state.show_login=True
        st.session_state.show_signup=False
with col3:
    if st.button("📝sign-up"):
        st.session_state.show_signup=True
        st.session_state.show_login=False


#executes if login button is clicked
if st.session_state.show_login: 
    #creating the login form
    with st.form(key="login_page"):
        st.subheader("LOGIN:",width="content",divider="yellow")
        username=st.text_input("👤USERNAME:").strip()
        psword=st.text_input("🔑PASSWORD:",type="password").strip() #type:password masks password
        submit=st.form_submit_button() #form will not run without submit button
    if submit:
        if psword=="" and username=="":
            st.info("Please enter the required details")
        elif username=="":
            st.info("Please enter you username")
        elif psword=="":
            st.info("please enter your password")
        else:
            content=sheet.get_all_records()
            for user in content:
                if user["username"] == username and user["password"] == psword:
                    st.toast("Login successful", icon="✅")
                    # Set authentication state
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    # Redirect to dashboard
                    st.switch_page("dashboard.py")
                    break
            else:
                st.warning("invalid username or password")
                st.info("click on sign-up to create a new account")

#executes if signup button is clicked
spcl_char=["-","_","@"]  #list to store the special characters that are allowed in username
if st.session_state.show_signup:
    with st.form(key="create your account"):
        st.subheader("sign-up:",width="content",divider="yellow")
        new_username=st.text_input("👤USERNAME:").strip()
        new_password=st.text_input("🔑Set password:",type="password").strip()
        confirm_password=st.text_input("🛡️Confirm password:",type="password").strip()
        register=st.form_submit_button()
    if register:
        if new_username=="" and confirm_password=="":
            st.info("please enter the required details")
        elif new_username=="":
            st.info("please set a username")
        elif confirm_password=="":
            st.info("please set a password")
        elif confirm_password=="": 
            st.info("please confirm your password")
        elif new_password!=confirm_password:
            st.warning("passwords do not match")
        
        pattern = r'^[A-Za-z0-9_@]+$'
        if not re.match(pattern, new_username):
            st.warning("Username can only contain letters, numbers, '_' and '@'")
    
        elif len(new_username)>15:
            st.info("username cannot not have more than 15 characters")
        elif len(new_username)<6:
            st.info("username cannot not have less than 6 characters")
            
        pattern_pwd = r'^(?=.*[A-Z])(?=.*\d)(?=.*[_@])[A-Za-z0-9_@]+$'
        if not re.match(pattern_pwd, confirm_password):
            st.warning("Password must contain at least 1 capital letter, 1 number, and 1 special character ('_' or '@')")
        elif len(confirm_password)<6 :
            st.info("password should be of minimum 6 characters")
        elif len(confirm_password)>15:
            st.info("password cannot have more than 15 characters")
        
        else:
            content=sheet.get_all_records()
            for user in content:
                if user["username"]==new_username:
                    st.info("This user already exits.Please click on login or enter different username")
                    break
            else:
                sheet.append_row([new_username,confirm_password])
                st.toast("Registered Successfully", icon="✅")
                # Set authentication state
                st.session_state.authenticated = True
                st.session_state.username = new_username
                # Redirect to dashboard
                st.switch_page("dashboard.py")

                



                    

