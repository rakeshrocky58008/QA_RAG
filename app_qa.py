import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant answering queries."),
        ("user", "Question: {question}")
    ]
)

# Function to generate responses
def generate_response(question, model):
    chain = prompt | model
    answer = chain.invoke({'question': question})
    return answer

# Initialize the Groq model
def initialize_model(engine, api_key):
    return ChatGroq(groq_api_key=api_key, model_name=engine)

# Main app function
def main():
    # Select model and parameters
    model_engine = st.sidebar.selectbox("Select Groq model", ["Gemma2-9b-It", "AnotherGroqModel"])
    temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
    max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

    # Initialize model with selected settings
    model = initialize_model(engine=model_engine, api_key=api_key)

    # Initialize a placeholder for user input in session state
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    # Function to handle input submission
    def submit_question():
        # Fetch the response
        response = generate_response(st.session_state.user_input, model)
        st.write("Assistant:", response.content)
        
        # Clear the input field by setting it to an empty string
        st.session_state.user_input = ""

    # Main chat interface
    st.write("Ask any question below:")

    # Create the text input field that updates session state
    st.text_input("You:", key="user_input", on_change=submit_question)

    # Display prompt for input
    if not st.session_state.user_input:
        st.write("Please enter a question.")

# Run the main function
if __name__ == "__main__":
    st.sidebar.header("Settings")
    main()
