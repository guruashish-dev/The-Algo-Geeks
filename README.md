# Lifeline AI Chatbot

Lifeline AI Chatbot is an AI-powered first aid assistant designed to provide instant responses to medical emergencies and first-aid-related queries. The chatbot uses **Gemini API** for AI processing and a **Node.js Express backend** to handle communication between the frontend and AI model.

## 🚀 Features
- 💬 **AI-powered First Aid Assistance** using Gemini API
- ⚡ **Real-time chat interface** with a user-friendly design
- 🌍 **Runs locally** with API-based AI responses
- 🛠 **Simple HTML, CSS, and JavaScript frontend**
- 🏗 **Node.js Express backend** for API communication

## 🏗 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/lifeline-ai-chatbot.git
cd lifeline-ai-chatbot
```

### 2️⃣ Get Access to Gemini API
- Sign up for **Gemini API** at [Google AI Studio](https://ai.google.dev/).
- Obtain an API key from Google.

### 3️⃣ Install Backend Dependencies
Ensure you have **Node.js** installed, then run:
```sh
npm install
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add your API key:
```env
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Start the Backend Server
```sh
node server.js
```
Server will run at: `http://localhost:5000`

### 6️⃣ Run the Frontend
Simply open `index.html` in your browser.

---

## 🔧 Usage
1. Open `index.html` in a web browser.
2. Type your first aid-related query.
3. The chatbot will respond with AI-generated advice.

---

## 📂 Project Structure
```
📁 lifeline-ai-chatbot
├── 📄 index.html        # Frontend UI
├── 📄 styles.css        # Styling
├── 📄 script.js         # Chat functionality
├── 📄 server.js         # Node.js backend (Express + Gemini API)
├── 📄 .env              # API key configuration
└── 📄 README.md         # Documentation
```

---

## 🚀 Future Enhancements
- 🌐 Deploy backend to a cloud server (Render/Heroku)
- 🎤 Add voice input and text-to-speech
- 📊 Improve AI responses with fine-tuned prompts

---

## 💡 Contributing
Feel free to fork this project, submit issues, and contribute enhancements!

---

## 📜 License
This project is licensed under the **MIT License**.

---

Made with ❤️ by **[Your Name]**

