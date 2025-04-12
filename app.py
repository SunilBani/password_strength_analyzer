from flask import Flask, render_template, request
from utils import calculate_password_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form["password"]
        strength, feedback = calculate_password_strength(password)
        return render_template("result.html", password=password, strength=strength, feedback=feedback)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
