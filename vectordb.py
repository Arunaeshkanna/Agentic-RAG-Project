import os
import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DB_PATH = "vector_store"

@st.cache_resource(show_spinner=False)
def get_vector_db():
    os.makedirs(DB_PATH, exist_ok=True)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )