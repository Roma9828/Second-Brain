import streamlit as st
from login import login_page
from main_app import main_app

st.set_page_config(page_title="AI Second Brain", layout="wide")

# Session states
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Routing
if st.session_state.logged_in:
    main_app()
else:
    login_page()