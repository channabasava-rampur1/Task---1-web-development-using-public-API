from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Initialize Flask
app = Flask(__name__)

# Configure Gemini API Key
genai.configure(api_key="YOUR_API_KEY_HERE")

# Model
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json.get("query")
    response = model.generate_content(user_query)
    return jsonify({"answer": response.text})

if __name__ == "__main__":
    app.run(debug=True)
