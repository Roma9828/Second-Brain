import streamlit as st
from utils import extract_text, split_text, get_answer

def main_app():

    # Sidebar
    st.sidebar.title("🧠 AI Second Brain")
    st.sidebar.write(f"Welcome, {st.session_state.username} 👋")

    menu = st.sidebar.selectbox("Menu", ["Home", "History", "Logout"])

    # Session states
    if "chat" not in st.session_state:
        st.session_state.chat = []
    if "chunks" not in st.session_state:
        st.session_state.chunks = []

    # ---------------- HOME ---------------- #
    if menu == "Home":

        st.title("🤖 AI Second Brain")

        uploaded_file = st.sidebar.file_uploader("Upload PDF", type="pdf")

        if uploaded_file:
            text = extract_text(uploaded_file)
            st.session_state.chunks = split_text(text)
            st.sidebar.success("PDF Ready ✅")

        if st.sidebar.button("🗑 Clear Chat"):
            st.session_state.chat = []

        # Chat display
        for role, msg in st.session_state.chat:
            with st.chat_message("user" if role == "You" else "assistant"):
                st.markdown(msg)

        # Input
        question = st.chat_input("Ask something...")

        if question:
            if st.session_state.chunks:

                with st.spinner("Thinking... 🤖"):
                    answer = get_answer(question, st.session_state.chunks)

                st.session_state.chat.append(("You", question))
                st.session_state.chat.append(("AI", answer))
                st.rerun()
            else:
                st.warning("Upload a PDF first!")

    # ---------------- HISTORY ---------------- #
    elif menu == "History":

        st.title("📜 Chat History")

        if st.session_state.chat:
            for role, msg in st.session_state.chat[::-1]:
                st.write(f"**{role}:** {msg}")
        else:
            st.info("No history yet!")

    # ---------------- LOGOUT ---------------- #
    elif menu == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()