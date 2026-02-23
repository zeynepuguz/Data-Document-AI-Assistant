# Data Document Assistant

A Retrieval-Augmented Generation (RAG) system that indexes PDF documents using OpenAI Vector Stores and answers questions strictly based on the provided documents.

The system uses:

- OpenAI GPT-4o
- File Search tool
- Vector Store indexing
- Guardrails to prevent hallucination

---

## 🚀 Features

- Upload and index PDF documents
- Semantic search over documents
- Answers restricted to document content only
- Source reporting
- Safe fallback: If information is not found, the system explicitly states it

---

---

## ⚙️ Installation

```bash
python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -U openai python-dotenv

Index Documents

Place your PDF files inside the documents/ folder.

Then run:

python scripts/index_docs.py

The script will output a vs_... vector store ID.

❓ Ask Questions
python scripts/ask.py vs_XXXXXXXX "What are the differences between CNN and RNN?"

The assistant will:

Search only within indexed documents

Refuse to answer if the information is not found

Optionally display document sources

🧠 Guardrail Behavior

If the answer is not found inside the provided documents, the assistant returns:

This information is not available in the provided documents.
🖥 Example Output

The example above shows:

A successful document-based answer

A safe fallback response when the answer is not found

Source extraction behavior

🛠 Tech Stack

Python

OpenAI GPT-4o

OpenAI Vector Store

File Search Tool

📌 Author

Built as a practical RAG implementation using OpenAI's file_search + vector store architecture.