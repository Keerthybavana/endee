import PyPDF2
from utils import add_document, search

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def main():
    print("📄 AI Smart Document Assistant (Endee-based RAG)\n")

    pdf_path = input("Enter PDF file path: ")
    
    print("\n⏳ Reading document...")
    text = extract_text_from_pdf(pdf_path)

    print("📥 Storing in vector database...")
    add_document(text)

    while True:
        query = input("\n💬 Ask a question (or type 'exit'): ")
        
        if query.lower() == 'exit':
            break

        result = search(query)
        print("\n📌 Answer:\n", result)

if __name__ == "__main__":
    main()