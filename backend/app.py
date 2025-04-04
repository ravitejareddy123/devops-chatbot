# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = ollama.chat(model='devops-chatbot', messages=[{"role": "user", "content": user_input}])
    return jsonify({"response": response["message"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)