from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_document(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def create_chunks(text: str, chunk_size=100, chunk_overlap=20) -> list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)


def load_and_create_chunks(file_path: str, chunk_size=1000, chunk_overlap=200) -> list:
    text = load_document(file_path)
    chunks = create_chunks(text, chunk_size, chunk_overlap)
    return chunks


if __name__ == "__main__":
    file_path = "D:\\Sagar\\bank of maharashtra loans gen ai project\\loans data\\document.txt"
    
    chunks = load_and_create_chunks(file_path, chunk_size=1000, chunk_overlap=200)

    print(f"Total chunks created: {len(chunks)}\n")
    for i, chunk in enumerate(chunks[:5]):  # show first 5 chunks
        print(f"--- Chunk {i+1} ---\n{chunk}\n")
