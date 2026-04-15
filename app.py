from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import re
from openai import OpenAI

# -------------------- SETUP --------------------
load_dotenv()
app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------- ADVANCED SYSTEM PROMPT --------------------
SYSTEM_PROMPT = """
You are an Advanced AI Customer Support Agent.

Name: Aivy 😊

🎯 ROLE:
Handle ONLY customer support queries (orders, payments, delivery, accounts)

❌ If NOT related:
"I'm here to assist only with customer support queries 😊"

🧠 RULES:
- Be polite, friendly
- Use emojis 😊
- No hallucination
- Ask if unclear

🧩 RESPONSE FORMAT:
1. Greeting
2. Understand issue
3. Steps / answer
4. Closing

🛠 TOOL RULE:
If order ID is mentioned → use provided order data

💢 ANGRY USERS:
Stay calm + empathetic

🏁 Always end with:
"Let me know if you need anything else 😊"

Think step-by-step internally, but return only final answer.
"""

# -------------------- MEMORY --------------------
message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# -------------------- FAKE DATABASE --------------------
ORDERS = {
    "123": {"status": "Shipped", "delivery": "20 April"},
    "456": {"status": "Processing", "delivery": "25 April"}
}

# -------------------- HELPER --------------------
def get_order_details(order_id):
    return ORDERS.get(order_id)

def extract_order_id(text):
    match = re.search(r"\b\d{3,6}\b", text)
    return match.group() if match else None

# -------------------- FRONTEND ROUTE --------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------- CHAT ROUTE --------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    # -------------------- ORDER DETECTION --------------------
    order_id = extract_order_id(user_input)

    if order_id:
        order = get_order_details(order_id)

        if order:
            reply = f"""Hi there! 😊

I found your order details:

📦 Order ID: {order_id}  
📌 Status: {order['status']}  
🚚 Expected Delivery: {order['delivery']}

Let me know if you need anything else 😊"""
        else:
            reply = """Hi! 😊

I couldn't find that order ID. Please check and try again.

Let me know if you need anything else 😊"""

        return jsonify({"reply": reply})

    # -------------------- NORMAL AI FLOW --------------------
    message_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=message_history,
        temperature=0.7
    )

    reply = response.choices[0].message.content

    message_history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})

# -------------------- RUN --------------------
if __name__ == "__main__":
    app.run(debug=True)