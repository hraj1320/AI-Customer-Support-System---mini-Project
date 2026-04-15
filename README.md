# 🤖 Aivy AI Customer Support System

An advanced AI-powered customer support chatbot built using **Flask + OpenAI API + Tailwind CSS**.
This system handles customer queries like orders, delivery, payments, and accounts with a professional UI/UX.

---

## 🚀 Features

* ✅ AI-powered customer support assistant
* ✅ Order tracking system (with order ID detection)
* ✅ Smart conversation memory
* ✅ Professional chat UI (Tailwind CSS + Glassmorphism)
* ✅ Typing animation & smooth UX
* ✅ Rule-based + AI hybrid system
* ✅ Handles angry users politely 😊
* ✅ Restricts responses to customer support domain

---

## 🧠 How It Works

1. User sends a message from frontend
2. Backend checks:

   * If **order ID exists** → fetch from database
   * Else → send to OpenAI model
3. AI generates structured response
4. Response is displayed in UI

---

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, Tailwind CSS, JavaScript
* **AI Model:** OpenAI (gpt-4.1-mini)
* **Environment:** dotenv

---

## 📂 Project Structure

```
project/
│── app.py
│── .env
│── requirements.txt
│
├── templates/
│   └── index.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/aivy-ai-support.git
cd aivy-ai-support
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the App

```bash
python app.py
```

App will run on:

```
http://127.0.0.1:5000/
```

---

## 📦 Example Order Data

| Order ID | Status     | Delivery Date |
| -------- | ---------- | ------------- |
| 123      | Shipped    | 20 April      |
| 456      | Processing | 25 April      |

---

## 💬 Example Queries

* "Where is my order 123?"
* "My payment failed"
* "I want to track my delivery"

---

## 🔐 Rules Implemented

* Only customer support queries allowed
* No hallucination responses
* Structured replies
* Friendly tone with emojis 😊

---

## 🚀 Future Improvements

* 🔹 Chat history (like ChatGPT)
* 🔹 Voice input 🎤
* 🔹 File upload (PDF/Image)
* 🔹 Real-time streaming responses
* 🔹 Database integration (MongoDB / PostgreSQL)
* 🔹 Authentication system

---

## 🤝 Contributing

Feel free to fork this project and improve it.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 💡 Author

**Himanshu Kumar**
Aspiring DevOps & AI Engineer 🚀

---

⭐ If you like this project, don't forget to star the repo!
