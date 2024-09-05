from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
import google.generativeai as genai

#API key
genai.configure(api_key="AIzaSyCSfMABLQ2kHa9_m3YdiITesLIF0b6guXU")

#skill-horizon-bot v1.0
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

class ChatbotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up the main layout
        self.layout = QVBoxLayout()
        
        # Create chat display area
        self.chat_window = QTextEdit()
        self.chat_window.setReadOnly(True)
        self.chat_window.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;                                
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 10px;
                font-family: 'Comic Sans MS';
                font-size: 12pt;
            }
        """)
        # Customizing the scroll bar
        self.chat_window.setStyleSheet("""
            QTextEdit {
                background-color: #36b8ff;
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 10px;
                font-family: 'Comic Sans MS';
                font-size: 14pt;
            }
            QTextEdit::verticalScrollBar {
                border: 1px solid #ddd;
                background: #f1f1f1;
                width: 12px;
            }
            QTextEdit::verticalScrollBar::handle {
                background: #007bff;
                border-radius: 6px;
            }
            QTextEdit::verticalScrollBar::handle:pressed {
                background: #0056b3;
            }
        """)
        self.layout.addWidget(self.chat_window)
        
        # Create user input and button layout
        self.input_layout = QHBoxLayout()
        
        # Create user input field
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Type a message...")
        self.user_input.setStyleSheet("""
            QLineEdit {
                border-radius: 15px;
                padding: 10px;
                border: 1px solid #ccc;
                font-family: 'Comic Sans MS';
                font-size: 14pt;
            }
        """)
        self.input_layout.addWidget(self.user_input)
        
        # Create send button
        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("""
            QPushButton {
                border-radius: 15px;
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                border: none;
                font-family: 'Comic Sans MS';
                font-size: 12pt;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.send_button.clicked.connect(self.send_message)
        self.input_layout.addWidget(self.send_button)
        
        # Add input layout to the main layout
        self.layout.addLayout(self.input_layout)
        
        # Set up the main window
        self.setLayout(self.layout)
        self.setWindowTitle("skill-horizon-bot v1.0")
        self.setGeometry(100, 100, 500, 600)
        self.show()

        # Bind Enter key to send message
        self.user_input.returnPressed.connect(self.send_message)

    def send_message(self):
        user_text = self.user_input.text().strip()
        if user_text:
            self.chat_window.append(" ")
            self.chat_window.append(f"<b>User :</b> {user_text}")
            bot_response = self.get_bot_response(user_text)
            self.chat_window.append(f"<b>Bot :</b> {bot_response}")
            self.user_input.clear()
            self.chat_window.verticalScrollBar().setValue(self.chat_window.verticalScrollBar().maximum())

    def get_bot_response(self, user_input):
        response = chat.send_message(user_input)
        return response.text

if __name__ == "__main__":
    app = QApplication([])
    chatbot_app = ChatbotApp()
    app.exec_()
