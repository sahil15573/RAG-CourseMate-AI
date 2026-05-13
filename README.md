# 📚 RAG CourseMate AI

An AI-powered PDF Question Answering System built using **Retrieval-Augmented Generation (RAG)** architecture with **Mistral AI**, **Hugging Face Embeddings**, **ChromaDB**, **LangChain**, and **Streamlit**.

Users can upload PDFs and interact with documents conversationally using semantic search and AI-powered retrieval.

---

# 🚀 Live Demo

🔗 https://sahil15573-rag-coursemate-ai-app-k1vka0.streamlit.app/

---

# ✨ Features

- 📄 Upload and chat with PDFs
- 🤖 AI-powered conversational document retrieval
- 🔍 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Fast similarity search with ChromaDB
- 🎯 Context-aware responses using Mistral AI
- 💬 Interactive modern Streamlit UI
- ☁️ Fully deployed on Streamlit Cloud

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend / AI Framework
- LangChain

## LLM
- Mistral AI

## Embeddings
- Hugging Face Sentence Transformers

## Vector Database
- ChromaDB

## PDF Processing
- PyMuPDF

---

# 🧠 RAG Architecture

```text
User Query
     ↓
PDF Upload
     ↓
Document Chunking
     ↓
Hugging Face Embeddings
     ↓
ChromaDB Vector Storage
     ↓
Similarity Search
     ↓
Relevant Context Retrieval
     ↓
Mistral AI
     ↓
Final AI Response
```

---

# 📂 Project Structure

```text
RAG-CourseMate-AI/
│
├── app.py
├── main.py
├── create_database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── document_loaders/
│   └── deeplearning.pdf
│
└── venv/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sahil15573/RAG-CourseMate-AI.git
```

---

## 2️⃣ Navigate to Project

```bash
cd RAG-CourseMate-AI
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows (PowerShell)

```bash
venv\Scripts\activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

# ▶️ Run the Application

```bash
py -m streamlit run app.py
```

---

# 📦 Deployment

This project is deployed using:

- Streamlit Community Cloud
- GitHub Integration

---

# 🧩 Core Functionalities

## 📄 PDF Processing
- Extracts text from uploaded PDFs using PyMuPDF

## ✂️ Text Chunking
- Splits documents into smaller semantic chunks

## 🔍 Embedding Generation
- Generates embeddings using:
  - `sentence-transformers/all-MiniLM-L6-v2`

## 🗂️ Vector Storage
- Stores embeddings in ChromaDB

## 🤖 Conversational Retrieval
- Retrieves relevant chunks and generates answers using Mistral AI

---

# 🧪 Example Questions

```text
What is Deep Learning?

Summarize Chapter 2.

What are Neural Networks?

Explain Gradient Descent.
```

---

# 📈 Future Improvements

- Multi-PDF support
- Chat history memory
- Authentication system
- Persistent vector databases
- Streaming AI responses
- Voice input support
- Citation highlighting
- Multi-language support

---

# 🛡️ Challenges Solved

- PDF text extraction issues
- ChromaDB metadata filtering
- Streamlit deployment compatibility
- Embedding optimization
- Vector retrieval pipeline

---

# 🎯 Learning Outcomes

Through this project I learned:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- LLM Integration
- LangChain Pipelines
- Embedding Models
- Streamlit Deployment
- AI Application Development

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork this repository and submit pull requests.

---

# 👨‍💻 Author

## Sahil Kumar

- GitHub: https://github.com/sahil15573

- Email: sahilkr.15573@gmail.com

---

# ⭐ If You Like This Project

Please consider giving this repository a star ⭐
