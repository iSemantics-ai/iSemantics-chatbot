import os
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.messages.base import BaseMessage
from basic_chain import create_basic_chain, get_model
from splitter import split_documents
from vector_store import create_vector_db


def find_similar(vs, query):
    docs = vs.similarity_search(query)
    return docs

def format_docs(docs, separator='\n\n'):
    return separator.join([doc.page_content for doc in docs])

def get_question(input):
    if not input:
        return None
    elif isinstance(input, str):
        return input
    elif isinstance(input, dict) and 'question' in input:
        return input['question']
    elif isinstance(input, BaseMessage):
        return input.content
    else:
        raise Exception('string or dict with "question" key expected as RAG chain input')
    
def make_rag_cahin(model, retriever, rag_prompt=None):
    if not rag_prompt:
        rag_prompt = hub.pull('rlm/rag-prompt')
    
    # use LangChain RunnablePassthrough to add some custom processing into our chain.
    rag_chain = (
        {
            'context': RunnableLambda(get_question) | retriever | format_docs,
            'question': RunnablePassthrough()
        }
        | rag_prompt
        | model
    )
    
    return rag_chain
