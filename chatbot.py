import sys
import json
import os
import google.generativeai as genai
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

# ====== CONFIGURE API KEY HERE ======
API_KEY = "###########################"  # <-- put your API key here
genai.configure(api_key=API_KEY)

HISTORY_FILE = "chat_history.json"

# ====== LOAD CHAT HISTORY ======
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# ====== SAVE CHAT HISTORY ======
def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

# ====== GET AI RESPONSE ======
def get_ai_response(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

# ====== GUI CLASS ======
class ChatBotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Colorful ChatBot - Gemini AI")
        self.setGeometry(200, 100, 600, 700)

        # Color theme
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#1E1E2E"))
        palette.setColor(QPalette.Base, QColor("#2A2A3C"))
        palette.setColor(QPalette.Text, QColor("#FFFFFF"))
        self.setPalette(palette)

        layout = QVBoxLayout()

        title = QLabel("💬 Gemini AI ChatBot")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setStyleSheet("color: #FFB86C; padding: 10px;")
        layout.addWidget(title)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.chat_area.setFont(QFont("Arial", 12))
        self.chat_area.setStyleSheet("background-color: #2A2A3C; color: white; padding: 10px;")
        layout.addWidget(self.chat_area)

        self.input_box = QLineEdit()
        self.input_box.setFont(QFont("Arial", 12))
        self.input_box.setStyleSheet("background-color: #3A3A4F; color: white; padding: 8px; border-radius: 5px;")
        layout.addWidget(self.input_box)

        send_button = QPushButton("Send")
        send_button.setFont(QFont("Arial", 12, QFont.Bold))
        send_button.setStyleSheet("background-color: #50FA7B; padding: 8px; border-radius: 5px;")
        send_button.clicked.connect(self.send_message)
        layout.addWidget(send_button)

        self.setLayout(layout)

        # Load and show history
        self.history = load_history()
        self.display_history()

    def display_history(self):
        self.chat_area.clear()
        for chat in self.history:
            self.chat_area.append(f"🧑 You: {chat['user']}")
            self.chat_area.append(f"🤖 Bot: {chat['bot']}\n")

    def send_message(self):
        user_message = self.input_box.text().strip()
        if not user_message:
            return
        self.chat_area.append(f"🧑 You: {user_message}")
        self.input_box.clear()

        bot_response = get_ai_response(user_message)
        self.chat_area.append(f"🤖 Bot: {bot_response}\n")

        # Save to history
        self.history.append({"user": user_message, "bot": bot_response})
        save_history(self.history)


# ====== RUN APP ======
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatBotGUI()
    window.show()
    sys.exit(app.exec_())

