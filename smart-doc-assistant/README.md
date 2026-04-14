# 📄 AI Smart Document Assistant (RAG using Endee Concept)

## 🚀 Project Overview

This project is an AI-powered document assistant that allows users to upload PDF files and ask questions about their content.

It uses a Retrieval-Augmented Generation (RAG) approach with vector embeddings to retrieve relevant information from documents and provide accurate responses.

---

## 🧠 Features

* Upload and process PDF documents
* Ask questions about document content
* Semantic search using embeddings
* Retrieval-based answering system

---

## ⚙️ Technologies Used

* Python
* Sentence Transformers
* NumPy
* PyPDF2
* Vector Database Concept (inspired by Endee)

---

## 🏗️ System Architecture

User → Upload PDF
→ Text Extraction
→ Chunking
→ Embedding Generation
→ Vector Storage
→ Query Input
→ Similarity Search
→ Relevant Answer Output

---

## 📌 How Endee is Used

The project follows the core idea of a vector database as implemented in Endee.

* Text is converted into embeddings
* Embeddings are stored in a vector-like structure
* Similarity search is used to retrieve relevant content

---

## ▶️ How to Run

1. Clone the repository
2. Navigate to project folder

```bash
cd smart-doc-assistant
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python app.py
```

5. Enter PDF path and ask questions

---

## 📂 Example

Input:

```
What is this document about?
```

Output:

```
Relevant extracted content from the document
```

---

## 🎯 Future Improvements

* Add support for multiple documents
* Improve answer generation using LLM APIs
* Add web interface

---

## 👩‍💻 Author

Keerthana P
