QARAG



This repository contains a multi-page Streamlit application that provides two main functionalities:
Home Page: A primary interface for general interactions.
Q&A Chatbot: A chatbot that interacts with users and answers questions based on the context of provided documents using Groq-powered language models.

Features
Navigation Sidebar: Users can easily switch between the "Home" page and the "Q&A Chatbot" page using a sidebar radio button.
Home Page (app.py): A chatbot interface where users can input questions and receive AI-generated answers, leveraging advanced language models.
Q&A Chatbot Page (app_qa.py): A RAG Application for PDF Q&A


HOW TO USE : 


The webapp has two functionalities 

1. A Q&A chat bot from gemma 8b parameter by Google interface
    * You can set the temperature and Max tockens for the App so u can maintain your free limit on Gemma
      
3. A PDF RAG with Session history , for Q&A on uploaded document
    * Provision for privacy with Groq api , user can use their own APi from Groq so its secure or you the default one which is free tier version
    * Just upload the PDF and wait it to prompt for a Question !!
      



How to Run the App : 

1. In local Machine 
    Using Docker Image -  https://hub.docker.com/r/rakeshz12/qa_rag_app 

     Pull image from docker hub 
        docker pull rakeshz12/qa_rag_app:linux
     Run Command below to Run -
        docker run -d --expose=8501 rakeshz12/qa_rag_app:linux
   
     view using localhost - http://localhost:8501

 2. In Azure Webapp

    Using Azure Webapp we can deploy application.

    Create Azure Web App for Containers
      This is the easiest way to deploy a Docker container on Azure.

      1. In the Azure Portal, search for App Services and click Create.
         
      Under Basics:
      Choose the Subscription and Resource Group.
      Set the Name for your app (this will become part of your app's URL, e.g., myapp.azurewebsites.net).
      Select Docker Container for the Publish option.
      Choose Linux as the Operating System.
      Under Region, choose the closest region to your users.
      Under SKU and Size, select B1 (Basic) or Free for testing (you can scale up later).
       Configure Docker Settings
      
      2. In the Docker tab:
        Select Single Container.
        Choose Azure Container Registry if you’re using ACR, Docker Hub if your image is on Docker Hub, or Other Registry for any other container registry.
        Enter the Image and Tag (e.g., your_image_name:v1) if it’s not automatically populated.

        rakeshz12/qa_rag_app:linux

      4. Set Environment Variables and Ports
          In the Settings tab, go to Configuration.
          Add a new application setting with:
          Key: WEBSITES_PORT
          Value: 8501 (Streamlit’s default port)
          Save changes.
          7. Review and Create
          Review your configuration and click Create.
          Azure will deploy your container, which may take a few minutes.

      5. Access Your Deployed App
      Once deployed, navigate to App Services in the Azure Portal.
      Click on your web app, and under Overview, you’ll see the URL (e.g., https://<webapp-name>.azurewebsites.net). Use this URL to access your app.



     

Build the App :


Prerequisites -
Python 3.11+ (Ensure compatibility with all required libraries)
Streamlit and additional dependencies specified in requirements.txt

Installation Steps -
Clone this repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run main_app.py



Directory Structure - 
.
├── app.py              # Home page functionality
├── app_qa.py           # Q&A Chatbot functionality
├── main_app.py         # Combines both pages and handles navigation
├── requirements.txt    # Required Python libraries
├── .env                # Environment variables (ensure it's secure)
└── README.md           # This README file


Usage - 

Home Page: Provides a welcoming interface and possibly other features.

Q&A Chatbot Page:
Enter questions in the input field.

The chatbot responds with context-aware answers, using Groq-powered models.


Customization - 
Modify app.py and app_qa.py to add or adjust the content and features.
Update main_app.py to include more pages or adjust navigation.


Tech Stack
Streamlit: Used to build the interactive web app.
Groq-powered Language Models: Utilized for generating responses.
HF - hugging face libraries 
Python: The programming language for developing the application 
logic.


Environment Variables
Ensure you have a .env file with the following environment variables set:
makefile
Copy code
GROQ_API_KEY=your_groq_api_key
HF_KEY=your_HF_key


ScreenShots - 

QA PAGE 
![image](https://github.com/user-attachments/assets/881c77da-d3a4-4bc8-a676-850cd5fe6a35)

RAG PAGE 

![image](https://github.com/user-attachments/assets/e8b4122a-5f48-4923-9029-b0c6ce763974)



