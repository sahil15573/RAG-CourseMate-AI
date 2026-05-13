# app.py

import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="RAG CourseMate AI",
    page_icon="📚",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stApp {
    background: linear-gradient(to bottom right, #0E1117, #111827);
    color: white;
}

.title {
    font-size: 3rem;
    font-weight: 700;
    color: #FFFFFF;
}

.subtitle {
    font-size: 1.2rem;
    color: #B3B3B3;
}

.chat-box {
    padding: 1rem;
    border-radius: 12px;
    margin-bottom: 1rem;
}

.user-chat {
    background-color: #1E293B;
}

.ai-chat {
    background-color: #111827;
    border: 1px solid #374151;
}

.stButton>button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
}

.stButton>button:hover {
    background-color: #1D4ED8;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOAD ENV
# =========================
load_dotenv()

# =========================
# HEADER
# =========================
st.markdown(
    """
    <div class="title">📚 RAG CourseMate AI</div>
    <div class="subtitle">
    Upload your PDF and chat with your documents using Mistral AI + Hugging Face Embeddings.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# =========================
# SIDEBAR
# =========================
with st.sidebar:

    st.header("⚙️ Settings")

    st.markdown("""
    ### 🤖 Tech Stack

    - Mistral AI
    - Hugging Face Embeddings
    - ChromaDB
    - LangChain
    - Streamlit
    """)

    st.divider()

    uploaded_file = st.file_uploader(
        "📄 Upload Your PDF",
        type="pdf"
    )

# =========================
# SESSION STATE
# =========================
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================
# PROCESS PDF
# =========================
if uploaded_file is not None:

    with st.spinner("📚 Processing PDF and creating embeddings..."):

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_pdf_path = tmp_file.name

        # Load PDF
        loader = PyMuPDFLoader(temp_pdf_path)
        docs = loader.load()

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(docs)

        # Fix Chroma metadata issue
        chunks = filter_complex_metadata(chunks)

        # IMPORTANT CHECK
        if not chunks:
            st.error("No text could be extracted from this PDF.")
            st.stop()

        # Embedding model
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Create vector store
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model
        )

        st.session_state.vectorstore = vectorstore

    st.success("✅ PDF processed successfully!")

# =========================
# CHAT INTERFACE
# =========================
if st.session_state.vectorstore is not None:

    query = st.chat_input("Ask a question about your PDF...")

    if query:

        # Add user message
        st.session_state.chat_history.append(
            {"role": "user", "content": query}
        )

        # Retrieve documents
        retriever = st.session_state.vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 4,
                "fetch_k": 10,
                "lambda_mult": 0.5
            }
        )

        docs = retriever.invoke(query)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        # Prompt
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are RAG CourseMate AI.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say:
"I could not find the answer in the document."
"""
                ),
                (
                    "human",
                    """
Context:
{context}

Question:
{question}
"""
                )
            ]
        )

        final_prompt = prompt.invoke({
            "context": context,
            "question": query
        })

        # LLM
        llm = ChatMistralAI(
            model="mistral-small-latest",
            api_key=os.getenv("MISTRAL_API_KEY")
        )

        # Generate response
        with st.spinner("🤖 Thinking..."):
            response = llm.invoke(final_prompt)

        ai_response = response.content

        # Add AI response
        st.session_state.chat_history.append(
            {"role": "assistant", "content": ai_response}
        )

# =========================
# DISPLAY CHAT
# =========================
for message in st.session_state.chat_history:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="chat-box user-chat">
            <b>🧑 You:</b><br><br>
            {message['content']}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="chat-box ai-chat">
            <b>🤖 CourseMate AI:</b><br><br>
            {message['content']}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# FOOTER
# =========================
st.divider()

st.caption(
    "Built with ❤️ using Mistral AI, Hugging Face, ChromaDB, LangChain & Streamlit"
)