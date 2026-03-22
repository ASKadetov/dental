from flask import Flask, render_template, request, redirect, flash
import os
import requests


app = Flask(__name__)
app.secret_key = "secret"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GOOGLE_DOC_URL = "https://docs.google.com/document/d/1dyooE_Kcp7Lupr7IONs_FLKXEcW0lqU2/edit?rtpof=true&sd=true&tab=t.0"

@app.context_processor
def inject_globals():
    return dict(GOOGLE_DOC_URL=GOOGLE_DOC_URL)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contacts", methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        question = request.form.get("question")
        email = request.form.get("email")
        phone = request.form.get("phone")

        message = f"""
📩 Новый вопрос

❓ {question}
📧 {email}
📱 {phone}
"""
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            data={"chat_id": TELEGRAM_CHAT_ID, "text": message}
        )

        flash("Отправлено!")
        return redirect("/contacts")

    return render_template("contacts.html")