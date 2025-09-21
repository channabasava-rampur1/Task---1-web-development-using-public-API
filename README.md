# 🤖 Gemini Chatbot - AI-Powered Web Chat

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) ![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=flat-square&logo=google&logoColor=white)

---

### **Project Information**

- **Company:** CODTECH IT SOLUTION  
- **Intern Name:** Channabasava Rampur  
- **Intern ID:** CT06DY2265  
- **Domain:** Full Stack Web Development  
- **Duration:** 6 Weeks  
- **Mentor:** Neela Santhosh  

---

## 💬 Project Description

**Gemini Chatbot** is a simple AI-powered chatbot website that connects to **Google’s Gemini API**.  
Users can type questions or queries in the web interface, which are sent to the backend, and the AI’s response is displayed **in real-time**.

---

## ⚙️ How It Works

### **Frontend (Website UI)**

1. Users interact with a webpage that has a **text box** and a **button**.  
2. They type a question (e.g., “What is Python used for?”) and click **Ask**.  

### **Backend (Flask Server)**

1. Frontend sends the query to the Flask backend via a **POST request**.  
2. Flask acts as a bridge between the website and **Google Gemini API**.  
3. Backend sends the query to Gemini API using the **API key**.  
4. Gemini generates a response and sends it back to Flask.  
5. Backend returns the response to the frontend in **JSON format**.  
6. Website updates to show the **chatbot’s answer** under the text box.

---

## 🛠️ Tech Stack

| Frontend | Backend | AI Model |
|----------|---------|----------|
| HTML, CSS, JavaScript | Python, Flask | Google Gemini API |

---

## 🚀 How to Run

### **Clone the project**

```bash
git clone 
cd gemini-chatbot
Install dependencies
bash
Copy code
pip install flask google-generativeai
Add Gemini API Key
Edit app.py:

python
Copy code
genai.configure(api_key="YOUR_API_KEY_HERE")
Run the app
bash
Copy code
python app.py
Open in browser: http://127.0.0.1:5000

```

🌟 Features
Simple and clean UI

Real-time AI responses from Gemini

Backend powered by Flask

Easy to extend (add chat history or custom styling)

🔮 Future Improvements
Add chat history so users can view previous queries

Build a React frontend for a modern experience

Deploy to Render, Heroku, or Vercel for online access
---

## **output**

<img width="1912" height="861" alt="Image" src="https://github.com/user-attachments/assets/818fe5ad-5646-4395-8374-7b0af819cc14" />

---

<img width="1918" height="864" alt="Image" src="https://github.com/user-attachments/assets/42218b9d-58c4-46bd-b6c8-077259eb4c4e" />

---

<img width="1898" height="875" alt="Image" src="https://github.com/user-attachments/assets/98ba5f28-ee43-423b-980b-aba13da2aaca" />
