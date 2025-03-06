from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("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")

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response["choices"][0]["message"]["content"]
        return jsonify({"response": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
