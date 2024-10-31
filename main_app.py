import streamlit as st
import app  # Assuming app.py and app_qa.py are in the same directory
import app_qa

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "RAG PDF"])

# Display the selected page's content
if page == "Home":
    st.title("Home - Q&A App")
    app_qa.main()   # This calls the main function in app.py
elif page == "RAG PDF":
    st.header("RAG PDF")
    app.main()  # This calls the main function in app_qa.py
