# Gemini AI Chatbot(PyQt5)
This is a desktop chatbot application built using Google Gemini API and PyQt5. It provides a clean, colorful chat interface with persistent chat history.

# Features:
Google Gemini AI integration – Powered by google-generativeai
Modern PyQt5 interface – Dark theme with custom colors
Persistent chat history – Automatically saved and reloaded from chat_history.json
Lightweight single-file app – No backend required

# Requirements:
Python 3.9+ (recommended)
Google Gemini API key (Get one here)

# Install dependencies:
pip install google-generativeai PyQt5

⚒️ How to Run:
Set your Gemini API key
Open the code file and set your API key at the top:
API_KEY = "YOUR_API_KEY_HERE"

Run the app
python chatbot.py

# Start chatting!
* Type your message in the input box.
* Press Send to receive an AI-generated response.
* Previous chats are stored in chat_history.json.

⚒️ Project Structure:  
* chatbot.py           # Main PyQt5 app with Gemini integration
* chat_history.json    # (Auto-generated) stores previous conversations
* .env         # Your Gemini API Key

📝 Notes:
• If your API key is incorrect or missing, the chatbot will fail to respond.
• This app uses gemini-2.5-flash model. You can swap with other models if needed:
• model = genai.GenerativeModel("gemini-pro")
• Chat history is stored locally and not uploaded anywhere.

🪪 License:
• This project is for personal and educational use.
• Google Gemini API usage is subject to Google AI Terms of Service.
