### RAG DOCUMENT APP FOR PDF Query 

import streamlit as st
import os
import time
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.vectorstores import FAISS

def create_faiss_vectorstore(documents, embedding, retries=3, delay=2):
    for attempt in range(retries):
        try:
            # Try creating the FAISS vector store
            vectorstore = FAISS.from_documents(documents=documents, embedding=embedding)
            st.success("FAISS vectorstore created successfully.")
            return vectorstore
        except Exception as e:
            st.error(f"Attempt {attempt + 1} failed: {str(e)}")
            time.sleep(delay)
    st.error("Failed to create FAISS vectorstore after several attempts.")
    return None

def main():
    # Rest of your app.py code here
    # Replace st.title("RAK Q&A chatbot") with code under main()
    from dotenv import load_dotenv
    load_dotenv()
    os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
    os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
    os.environ['TOKENIZERS_PARALLELISM']="true"
    groq_api_key=os.getenv("GROQ_API_KEY")

    embeddings=HuggingFaceEmbeddings(model_name="all-MiniLm-L6-v2")
    #st.title("Convoversation RAG with pdf and chat history")
    st.write("Upload PDFs and chat with its contentx")

    st.sidebar.header("Settings")
    api_key = st.sidebar.text_input("Enter your Groq API key:", type="password", value=groq_api_key)
    api_key = api_key or groq_api_key  # Use provided API key or fallback to .env key
    model_engine = "Gemma2-9b-It"  # Fixed model for now, can be customized



    llm=ChatGroq(groq_api_key=api_key,model_name="Gemma2-9b-It")
    ## chat interface 
    session_id=st.text_input("Session Id",value="default_session")

    ### statefully manage chat history 

    if 'store' not in st.session_state:
        st.session_state.store={}
    uploaded_files=st.file_uploader("choose A PDF file",type="pdf",accept_multiple_files=True)

    ### Process uploaded PDS
    if uploaded_files:
        documents=[]
        for uploaded_file in uploaded_files:
            temp=f"./temp.pdf"
            with open(temp,"wb") as file:
                file.write(uploaded_file.getvalue())
                file_name=uploaded_file.name
            loader=PyPDFLoader(temp)
            docs=loader.load()
            documents.extend(docs)

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000,chunk_overlap=500)
        splits= text_splitter.split_documents(documents)
        vectorstore=create_faiss_vectorstore(splits,embeddings)
        if vectorstore:
            retriever = vectorstore.as_retriever()
            st.success("Retriever created successfully.")
        else:
            st.error("Could not initialize retriever.")
        
        contextualize_q_system_prompt=(
            "Given a chat history and the latest user question"
            "which might reference context in the chat history,"
            "formulate a standalone question which can be understood,"
            "without chat history . Do not answer question,"
            "just reformulate it ,if needed and otherwise return it as is."
        ) 

        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system",contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human","{input}")
            ]

        )

        history_aware_retriever=create_history_aware_retriever(llm,retriever,contextualize_q_prompt)  
        
        ### ans qstn prompt 

        system_prompt = (
            "You are an assistant for question answering tasks. "
            "Use the following pieces of retrieved context to answer"
            "the question .If you don't know the answerr , say that you"
            "don't know . Use three sentences maximum and keep answer concise.if the question is 'what is this shit' reply with 'FUCK you , what you mad about '\n\n"
            "{context}"
        )
        
        qa_prompt= ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human","{input}"),
            ]
        )

        question_answer_chain=create_stuff_documents_chain(llm,qa_prompt)

        rag_chain=create_retrieval_chain(history_aware_retriever,question_answer_chain)
        
        def get_session_history(session:str)->BaseChatMessageHistory:
            if session_id not in st.session_state.store:
                st.session_state.store[session_id]=ChatMessageHistory()
            return st.session_state.store[session_id]    
        

        conversational_rag_chain=RunnableWithMessageHistory(
            rag_chain,get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
        )

        user_input = st.text_input("Your question:")
        if user_input:
            session_history=get_session_history(session_id)
            response = conversational_rag_chain.invoke(
                {"input":user_input},
                config={
                    "configurable":{"session_id":session_id}
                },
            )
            st.write(st.session_state.store)
            st.write("Assistant:",response['answer'])
            st.write("Chat history:",session_history.messages)


if __name__ == "__main__":
    main()
