from flask import Flask, render_template, request, redirect, flash
import os
import requests


app = Flask(__name__)
app.secret_key = "secret"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GOOGLE_DOC_URL = "https://docs.google.com/document/d/1PL-zdFlLb-MkSX5A8a7n34v3_O7Btsbp/edit?usp=sharing&ouid=115948205042641805739&rtpof=true&sd=true"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/price")
def price():
    return render_template("price.html")

@app.route("/price-file")
def price_redirect():
    return redirect(GOOGLE_DOC_URL)

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