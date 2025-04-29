import os
import logging
import uuid
import json
import requests
import markdown2
from flask import Flask, request, jsonify, render_template, session
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
from flask_cors import CORS  # Import CORS

# Load environment variables
load_dotenv()

# OpenRouter setup
OPENROUTER_API_KEY = "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"  # Replace with your actual API key
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "deepseek/deepseek-r1:free"

LANGUAGES = {
    "en": "English", "hi": "Hindi", "ta": "Tamil", "bn": "Bengali",
    "te": "Telugu", "gu": "Gujarati", "kn": "Kannada", "ml": "Malayalam",
    "pa": "Punjabi", "ur": "Urdu", "mr": "Marathi"
}

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

app.secret_key = os.urandom(24)
app.config['SESSION_PERMANENT'] = False

logging.basicConfig(level=logging.INFO)

def get_session_id():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    if "chat_history" not in session:
        session["chat_history"] = []
    return session["session_id"]

@app.before_request
def reset_on_reload():
    session.modified = True
    if request.endpoint == 'home':
        session.clear()

@app.route('/')
def home():
    return render_template('index.html')

def home():
    return render_template('Constitutional-Rights-Contact-Page.html')

def home():
    return render_template('Legal-Topics-Overview (1).html')

def home():
    return render_template('Constitutional-Rights-Contact-Page.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if data.get('clear_history', False):
        if 'chat_history' in session:
            session['chat_history'] = []
        return jsonify({"status": "history_cleared"})
    user_query = data.get('query', '').strip()
    user_lang = data.get('lang', 'en')

    if not user_query:
        return jsonify({"response": "Please enter a valid question."})

    session_id = get_session_id()
    history = session.get("chat_history", [])

    try:
        translator_to_en = GoogleTranslator(source='auto', target='en')
        translator_to_user_lang = GoogleTranslator(source='en', target=user_lang)

        translated_query = translator_to_en.translate(user_query) if user_lang != "en" else user_query

        messages = [{"role": "system", "content": "You are a helpful legal assistant for Indian law. Answer as clearly as possible. Use short paragraphs and bullet points where needed. Do not use any emojis in answer."}]
        messages.extend([{"role": h["role"], "content": h["content"]} for h in history])
        messages.append({"role": "user", "content": translated_query})

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": MODEL,
            "messages": messages
        }
        response = requests.post(OPENROUTER_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()

        result = response.json()

        # ✅ Safe check
        if "choices" in result and isinstance(result["choices"], list) and len(result["choices"]) > 0:
            english_response = result["choices"][0]["message"]["content"].strip()
        else:
            error_message = result.get("error", {}).get("message", "Unexpected server error.")
            logging.error(f"OpenRouter API Error: {error_message}")
            return jsonify({"response": f"Sorry, server error: {error_message}"})

        translated_response = translator_to_user_lang.translate(english_response) if user_lang != "en" else english_response

        final_html_response = markdown2.markdown(translated_response)

        history.append({"role": "user", "content": user_query})
        history.append({"role": "assistant", "content": english_response})
        session["chat_history"] = history

        return jsonify({"response": final_html_response})

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return jsonify({"response": "Sorry, I couldn't connect to the server. Please check your internet connection and try again."})
    except Exception as e:
        logging.error(f"Chat error: {e}")
        return jsonify({"response": "Sorry, something went wrong. Please try again later."})

if __name__ == '__main__':
    app.run(debug=True)
