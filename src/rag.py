from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K_RESULTS,
    OPENAI_MODEL,
    VECTOR_DB_DIR,
)

class RAGSystem:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        self.vector_store = None
        self.llm = ChatOpenAI(model=OPENAI_MODEL)
        
    def create_vector_store(self, documents):
        """Create vector store from documents"""
        texts = self.text_splitter.split_documents(documents)
        self.vector_store = Chroma.from_documents(
            documents=texts,
            embedding=self.embeddings,
            persist_directory=str(VECTOR_DB_DIR)
        )
        
    def get_relevant_context(self, query):
        """Retrieve relevant context for the query"""
        if not self.vector_store:
            return ""
        
        docs = self.vector_store.similarity_search(query, k=TOP_K_RESULTS)
        return "\n".join(doc.page_content for doc in docs)
    
    def create_conversion_chain(self):
        """Create RAG chain for test conversion"""
        template = """You are a test case conversion expert. Convert the following C++ test case to Python PyTest format.
        
        Context from similar test cases:
        {context}
        
        C++ Test case to convert:
        {test_case}
        
        Provide the converted Python test case only, without any explanations."""
        
        prompt = ChatPromptTemplate.from_template(template)
        
        chain = (
            {"context": self.get_relevant_context, "test_case": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        
        return chain 