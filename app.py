from flask import Flask, render_template, request
import re
import string

app = Flask(__name__)

def calculate_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(rf"[{re.escape(string.punctuation)}]", password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$ etc.).")

    strength = "Weak"
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"

    return strength, feedback

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form["password"]
        strength, feedback = calculate_password_strength(password)
        return render_template("result.html", password=password, strength=strength, feedback=feedback)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

