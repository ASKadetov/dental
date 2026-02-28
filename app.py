from flask import Flask, render_template, redirect

app = Flask(__name__)

GOOGLE_DOC_URL = "https://drive.google.com/your_doc_link_here"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/prices")
def prices():
    return redirect(GOOGLE_DOC_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)