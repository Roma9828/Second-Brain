from pypdf import PdfReader
from groq import Groq
import streamlit as st

# Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Extract text from PDF
def extract_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Split into chunks
def split_text(text, chunk_size=800):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Get AI answer
def get_answer(question, chunks):

    relevant_chunks = [
        chunk for chunk in chunks
        if question.lower() in chunk.lower()
    ]

    if not relevant_chunks:
        relevant_chunks = chunks[:3]

    context = " ".join(relevant_chunks[:3])

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Answer only from the PDF. If not found, say 'Not in document'."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            }
        ]
    )

    return response.choices[0].message.content