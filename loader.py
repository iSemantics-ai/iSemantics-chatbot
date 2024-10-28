import json
import os
from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import WebBaseLoader

DATA_LOADERS = {'.pdf': PyPDFLoader, '.txt': TextLoader, '.csv': CSVLoader}

def correct_file_extension(file_extension):
    file_extension = file_extension if file_extension.startswith('.') else f'.{file_extension}'
    return file_extension
def list_files(file_extension, data_dir='./data'):
    file_extension = correct_file_extension(file_extension)
    paths = Path(data_dir).glob(f'*{file_extension}')
    for path in paths:
        yield str(path)
        
def load_files_text(file_extension=None, data_dir='./data', online=False):
    if file_extension=='web' and online:
        return load_web_page(data_dir=data_dir)
    else:
        file_extension = correct_file_extension(file_extension)
        docs = []
        for path in list_files(file_extension=file_extension, data_dir=data_dir):
            print(f'Loading {path}')
            loader = DATA_LOADERS[file_extension](path)
            docs.extend(loader.load())
        return docs

def load_web_page(data_dir='./urls.json'):
    with open(data_dir) as f:
        urls = json.load(f)
    urls = [x['url'] for x in urls]
    loader = WebBaseLoader(urls)
    docs = loader.load()
    return docs
