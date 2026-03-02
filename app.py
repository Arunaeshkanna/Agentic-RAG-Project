import streamlit as st
import os
from dotenv import load_dotenv
from ingestion import load_documents
from vectordb import get_vector_db
from rag_pipeline import generate_strict_answer
from agentic_pipeline import run_agentic_rag

import warnings
warnings.filterwarnings("ignore")

load_dotenv()

st.set_page_config(page_title="Agentic RAG", layout="wide")
st.title("📚 Intelligent Document-Based Agentic RAG System")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.sidebar.subheader("Mode")
mode = st.sidebar.radio(
    "Select Mode:",
    ["Standard RAG", "Agentic RAG"]
)

uploaded_files = st.sidebar.file_uploader(
    "Upload Documents",
    accept_multiple_files=True
)

urls = st.sidebar.text_area("Enter URLs").splitlines()

if st.sidebar.button("📥 Ingest Documents"):
    with st.spinner("Indexing documents..."):
        docs = load_documents(uploaded_files, urls)
        db = get_vector_db()
        db.add_documents(docs)
        db.persist()
        st.sidebar.success("Documents indexed successfully!")

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

query = st.chat_input("Ask your question")

if query:
    st.session_state.chat_history.append({"role": "user", "content": query})

    with st.chat_message("assistant"):
        with st.spinner("Generating answer..."):

            if mode == "Standard RAG":
                answer, sources, confidence = generate_strict_answer(query)
            else:
                answer, sources, confidence = run_agentic_rag(query)

            st.markdown("### 📌 Answer")
            st.write(answer)

            if sources:
                st.markdown("### 📄 Sources")
                for s in sources:
                    st.write(f"- {s}")

    st.session_state.chat_history.append(
        {"role": "assistant", "content": answer}
    )