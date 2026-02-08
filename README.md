# Google Gemini Chatbot (Streamlit)

A simple web-based chatbot built with **Streamlit** and **Google Gemini (Generative AI)** that allows users to generate text responses in real time using the **gemini-2.5-flash** model.

---

## 🚀 Features

* Interactive chat UI using Streamlit
* Uses Google Gemini Generative AI (`gemini-2.5-flash`)
* Maintains chat history with `st.session_state`
* Loading spinner while generating responses
* Simple and clean code structure

---

## 🛠️ Requirements

Make sure you have **Python 3.9+** installed.

Install the required libraries:

```bash
pip install streamlit google-generativeai
```

---

## 🔑 API Key Setup

You need a **Google Gemini API Key**.

1. Get your API key from **Google AI Studio**
2. Replace this line in the code:

```python
api = 'YOUR_API_KEY_HERE'
```

⚠️ **Security Note:**
Do **NOT** hardcode your API key in production.
Use environment variables instead.

---

## ▶️ How to Run

Run the Streamlit app using:

```bash
streamlit run chatBot.py
```

Then open the provided local URL in your browser.

---

## 📄 Code Overview

### 1️⃣ Configure Gemini API

```python
genai.configure(api_key=api)
```

### 2️⃣ Text Generation Function

```python
def Generate_Text(text):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(text)
    return response.text
```

### 3️⃣ Chat History Management

Uses `st.session_state.messages` to store:

* User messages
* Assistant responses

### 4️⃣ Chat UI

* `st.chat_input()` for user input
* `st.chat_message()` for displaying messages
* `st.spinner()` for loading state

---

## 🧠 Model Used

* **gemini-2.5-flash**

  * Fast
  * Free-tier friendly
  * Ideal for chatbots and real-time interaction

---

## 📦 Project Structure

```text
.
├── chatBot.py
├── README.md
└── requirements.txt (optional)
```

---

## 📌 Example Use Cases

* AI chatbot
* Text generation tool
* Learning project for Gemini API
* Prototype for AI-powered applications

---

## ⚠️ Limitations

* Free tier has quota limits
* No streaming token-by-token output (yet)
* API key is hardcoded (for demo only)

---

## 🔮 Future Improvements

* Streaming responses
* Environment variable for API key
* Model switching (flash ↔ pro)
* Rate-limit handling
* UI customization

---

## 📜 License

This project is for **educational purposes**.
You are free to modify and use it.

