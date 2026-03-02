# Agentic-RAG-Project

# 🎯 1️⃣ Overall Definition of the Project:
The Intelligent Document-Based Agentic RAG System is an AI-powered question-answering platform that enables users to upload documents and ask questions based strictly on the uploaded content.

The system combines:
1.Retrieval-Augmented Generation (RAG)
2.Multi-Agent AI (CrewAI)
3.Large Language Model (Groq LLaMA 3.1)
4.Vector Database (ChromaDB)
5.to ensure accurate, structured, and hallucination-free answers grounded only in the provided documents.

The system supports multiple file formats including:
PDF
DOCX
TXT
PPTX
Web URLs

It provides two modes:
Standard RAG
Agentic RAG (enhanced with intelligent agents)



# 🛠 3️⃣ Tech Stack Used (With Purpose)
Below is your complete tech stack with purpose explained clearly.
🖥 Frontend Layer
Streamlit
Purpose:
Builds interactive chatbot UI
Handles file uploads
Displays answers and sources
Manages session chat history
Allows switching between Standard and Agentic modes

🧠 Large Language Model
Groq (LLaMA 3.1-8B-Instant)
Purpose:
Generates document-grounded answers
Runs with temperature=0 for deterministic output
Performs query rewriting and answer polishing via agents

🤖 Agent Framework
CrewAI
Purpose:
Creates intelligent agents
Defines agent roles and tasks
Executes sequential reasoning workflows
Agents Used:
Query Optimization Agent
Answer Quality Controller Agent

🔍 Retrieval Framework
LangChain
Purpose:
Connects LLM with vector database
Manages document loading
Handles text splitting
Creates retrieval pipeline

🗂 Vector Database
ChromaDB
Purpose:
Stores document embeddings
Performs semantic similarity search
Persists data locally
Retrieves top-k relevant chunks

🧮 Embeddings Model
sentence-transformers/all-MiniLM-L6-v2
Purpose:
Converts text chunks into vector embeddings
Enables semantic search instead of keyword search



# 🧠 Clean Architecture Diagram
                 ┌─────────────────────┐
                 │   User Interface    │
                 │     (Streamlit)     │
                 └──────────┬──────────┘
                            │
                            ▼
                ┌─────────────────────┐
                │  Mode Selection     │
                │ Standard / Agentic  │
                └──────────┬──────────┘
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
┌──────────────────┐               ┌────────────────────┐
│   Standard RAG   │               │   Agentic RAG      │
└────────┬─────────┘               └─────────┬──────────┘
         │                                     │
         ▼                                     ▼
   Similarity Search                  Query Optimization Agent
         │                                     │
         ▼                                     ▼
   Strict LLM Answer                   Similarity Search
         │                                     │
         ▼                                     ▼
   Return Answer                        Strict LLM Answer
                                                │
                                                ▼
                                     Answer Quality Agent
                                                │
                                                ▼
                                       Final Output



