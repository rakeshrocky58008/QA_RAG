# QA_RAG
QA and RAG APP 
This repository contains a multi-page Streamlit application that provides two main functionalities:

Home Page: A primary interface for general interactions.
Q&A Chatbot: A chatbot that interacts with users and answers questions based on the context of provided documents using Groq-powered language models.
Features
Navigation Sidebar: Users can easily switch between the "Home" page and the "Q&A Chatbot" page using a sidebar radio button.
Home Page (app_qa.py): A chatbot interface where users can input questions and receive AI-generated answers, leveraging advanced language models.
Q&A Chatbot Page (app_qa.py): A RAG to upload PDF and obtain information relavent from document in QA format 


How to Run the App


Prerequisites
Python 3.11+ (Ensure compatibility with all required libraries)
Streamlit and additional dependencies specified in requirements.txt
Installation Steps
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
streamlit run main_app.py
Directory Structure
bash
Copy code
.
├── app.py              # Home page functionality
├── app_qa.py           # Q&A Chatbot functionality
├── main_app.py         # Combines both pages and handles navigation
├── requirements.txt    # Required Python libraries
├── .env                # Environment variables (ensure it's secure)
└── README.md           # This README file
Usage

Home Page: Provides a welcoming interface and possibly other features.
Q&A Chatbot Page:
Enter questions in the input field.
The chatbot responds with context-aware answers, using Groq-powered models.
Customization
Modify app.py and app_qa.py to add or adjust the content and features.
Update main_app.py to include more pages or adjust navigation.
Tech Stack
Streamlit: Used to build the interactive web app.
Groq-powered Language Models: Utilized for generating responses.
Python: The programming language for developing the application logic.
Environment Variables
Ensure you have a .env file with the following environment variables set:

makefile
Copy code
GROQ_API_KEY=your_groq_api_key
Screenshots
Add screenshots of the app for better visual reference.


