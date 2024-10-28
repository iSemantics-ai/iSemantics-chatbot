import json
from langchain_community.document_loaders import WebBaseLoader

def load_web_pages(data_dir='./urls.json'):
    with open(data_dir) as f:
        urls = json.load(f)
        
    urls = [x['url'] for x in urls]
    loader = WebBaseLoader(urls)
    docs = loader.load()
    return docs

docs = load_web_pages()

print(docs[1].page_content)