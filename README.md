*COMPANY* : CODTECH IT SOLUTION
*NAME* : CHANNABASAVA RAMPUR
*INTERN ID* : CT06DY2265
*DOMAIN* : FULL STACK WEB DEVELOPMENT
*DURATION* : 6 WEEKS
*MENTOR* : NEELA SANTHOSH


##Description 

Gemini Chatbot

This project is a simple AI-powered chatbot website that connects to Google’s Gemini API.
It allows users to type in any question or query through a web interface, sends it to the backend, and then displays the AI’s response in real time.

How it Works

Frontend (Website UI)

The user interacts with a webpage that has a text box and a button.

They type in a question, for example: “What is Python used for?”, and click Ask.

Backend (Flask Server)

The frontend sends the user’s query to the Flask backend using a POST request.

Flask acts as a bridge between the website and the Gemini API.

Gemini API Call

The backend forwards the query to Google’s Gemini AI model using the API key.

Gemini processes the query and generates a response.

Send Answer Back

The Flask backend receives the response.

It sends the response back to the frontend in JSON format.

Display to User

The website updates to show the chatbot’s answer under the text box.

Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python, Flask

AI Model: Google Gemini API

How to Run

Clone this project:

git clone <your-repo-link>
cd gemini-chatbot


Install dependencies:

pip install flask google-generativeai


Add your Gemini API Key in app.py:

genai.configure(api_key="YOUR_API_KEY_HERE")


Run the app:

python app.py


Open in browser:
http://127.0.0.1:5000

Features

Simple and clean UI

Real-time responses from Gemini

Backend powered by Flask

Easy to extend (can add chat history or styling)

Future Improvements

Add chat history so users can see previous questions.

Create a modern React frontend for a smoother experience.

Deploy to Render, Heroku, or Vercel so others can use it online.

##output

<img width="1912" height="861" alt="Image" src="https://github.com/user-attachments/assets/2353f411-4511-4a7d-8b6e-a938a565a2a8" />

<img width="1918" height="864" alt="Image" src="https://github.com/user-attachments/assets/23eb7aba-37e7-455f-9c74-b680b0ee93f8" />

<img width="1898" height="875" alt="Image" src="https://github.com/user-attachments/assets/dd588626-7b7f-4a5f-9e19-4f0d72c2c559" />
