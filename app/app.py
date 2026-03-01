import os
import requests
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GOOGLE_DOC_URL = "https://drive.google.com/your_doc_link_here"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contacts", methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        question = request.form.get("question")
        email = request.form.get("email")
        phone = request.form.get("phone")

        message = f"""
📩 Новый вопрос с сайта

❓ Вопрос: {question}
📧 Email: {email}
📱 Телефон: {phone}
"""

        send_to_telegram(message)
        flash("Сообщение отправлено!")
        return redirect("/contacts")

    return render_template("contacts.html")

@app.route("/prices")
def prices():
    return redirect(GOOGLE_DOC_URL)

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)