# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

ollama.base_url = "http://ollama:11434"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        response = ollama.chat(
            model='gemma:2b',
            messages=[{"role": "user", "content": user_input}]
        )
        return jsonify({"response": response["message"]["content"]})
    except Exception as e:
        return jsonify({"error": "Failed to process message", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
