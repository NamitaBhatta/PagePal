import os 
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

GROQ_API_KEY = os.getenv("GROQ_API_KEY")




def get_llm_chain(vectorstore):
    llm = ChatGroq(api_key=GROQ_API_KEY, 
    model="llama-3.3-70b-versatile"
    )
    
    retriver = vectorstore.as_retriever(search_kwargs={"k": 3})
    return RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff",
        return_source_documents=True,
        retriever=retriver
    )
    

