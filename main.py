import os

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/",
methods=["GET", "POST"])
def home():
   title = "LOVE AT FIRST SIGHT"
   writer = "MORGAN FRAMES"
   year   = "2026"
   message =""
   if request.method == "POST":
       username = request.form["username"]
       message = f"Welcome, {username} Thank you for visiting LOVE AT FIRST SIGHT!"
   return render_template("index.html", title=title, writer=writer, message=message, year=year)
@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")
@app.route("/lesson")
def lesson():
    return render_template("lesson.html")
@app.route("/chapter4")
def chapter4():
    return render_template("chapter4.html")
@app.route("/chapter3")
def chapter3():
    return render_template("chapter3.html")
@app.route("/chapter2")
def chapter2():
    return render_template("chapter2.html")
@app.route("/chapter1")
def chapter1():
    return render_template("chapter1.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=True,
    )