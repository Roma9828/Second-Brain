import streamlit as st

USERS = {"khushwant": "1234"}

def login_page():

    st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #141e30, #243b55);
    }
    .login-box {
        width: 400px;
        margin: auto;
        padding: 40px;
        background: #1E1E2F;
        border-radius: 15px;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
        text-align: center;
    }
    .login-title {
        font-size: 28px;
        font-weight: bold;
        color: white;
    }
    .login-subtitle {
        color: #ccc;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)

        st.markdown('<div class="login-title">🧠 AI Second Brain</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Login to continue</div>', unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username in USERS and USERS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid credentials ❌")

        st.markdown('</div>', unsafe_allow_html=True)