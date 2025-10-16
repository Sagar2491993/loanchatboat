from langchain.document_loaders import TextLoader

def load_document(file_path: str):
    loader = TextLoader(file_path, encoding='utf-8')
    docs = loader.load()
    return docs

#####################################

from doc_loader import load_document

docs = load_document('D:\\Sagar\\bank of maharashtra loans gen ai project\\loans data\\document.txt')

print(type(docs))
print(len(docs))
print(docs[0].page_content)
