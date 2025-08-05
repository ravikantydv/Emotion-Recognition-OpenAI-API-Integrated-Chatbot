# 😊 Emotion Recognition Chatbot 🤖

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenAI API](https://img.shields.io/badge/OpenAI-API-informational)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

> **Emotion-Recognition-OpenAI-API-Integrated-Chatbot**  
A lightweight chatbot that analyzes user input for **emotion (Positive / Negative)** using the **OpenAI GPT API** and responds accordingly. It acts as a smart companion for applications in mental health, customer support, and personal assistants.

---

## 🎯 Features

- ✅ Integrates OpenAI GPT API
- 💬 Detects sentiment: **Positive / Negative**
- 🧠 Context-aware responses
- 🌐 Simple web interface or terminal interface
- 🔒 Supports `.env` for API key security
- 🛠️ Easily extendable to classify more emotions

---

## 🧠 How It Works

The user types a message →  
The chatbot sends it to the OpenAI API →  
The model analyzes **sentiment** →  
The chatbot responds based on the **emotion detected**.

---

## 🛠️ Tech Stack

| Layer         | Tech                    |
|---------------|-------------------------|
| Language       | Python 3.8+             |
| NLP Model      | OpenAI GPT API (gpt-3.5 / gpt-4) |
| Interface      | Flask Integrated |
| Deployment     | Localhost       |
| Env Management | Python-dotenv          |

---

## 🔐 Environment Variables

Create a `.env` file in your project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
▶️ How to Run
✅ Step 1: Clone & Install

git clone https://github.com/yourusername/Emotion-Recognition-OpenAI-API-Integrated-Chatbot.git
cd Emotion-Recognition-OpenAI-API-Integrated-Chatbot
pip install -r requirements.txt
🧠 Step 2: Add .env with your OpenAI API Key
💬 Step 3: Start Chatbot

python chatbot.py
💡 Example

User: I am feeling hopeless and tired.
Bot: I'm really sorry to hear that you're feeling this way. You're not alone, and it's okay to feel overwhelmed sometimes. If you need help, I’m here to talk.

Emotion detected: Negative

User: I’m feeling amazing today! Everything is going great.
Bot: That’s wonderful to hear! I’m so glad you’re having a great day. Keep smiling 😊

Emotion detected: Positive
📈 Future Scope
🧠 Multiclass emotion detection (Anger, Joy, Sadness, etc.)

🌍 Integration with WhatsApp/Telegram/Twitter

📱 Mobile app version

🧾 Chat history & analytics dashboard

📦 Dependencies

openai
python-dotenv
(For GUI: flask Based UI)

🧪 Testing

python tests/test_emotion_analyzer.py
🙌 Contributing
Feel free to fork this repository and submit a pull request. If you'd like to contribute, check out the issues tab.

📄 License
This project is licensed under the MIT License – see the LICENSE file.

📬 Contact
Ravikant Yadav
📧 Email: [your_email@example.com]
📷 Instagram: @codewithravi_ai
🧑‍💻 LinkedIn: linkedin.com/in/yourprofile

“A chatbot that listens, understands, and connects with your emotions and gives.” ❤️
