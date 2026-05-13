from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("document_loaders/GRU.pdf")

docs = data.load()
print(docs[1].page_content) #2nd page of the pdf