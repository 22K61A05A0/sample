from flask import Flask, render_template_string, request

app = Flask(__name__)
@app.route("/")
def registration_form():
    return "Welcome"

@app.route("/submit", methods=["POST"])
def submit_form():
    # Extracting data from the form
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    gender = request.form["gender"]
    return f"Thank you for registering, {name}! Your email: {email}, Gender: {gender}"

if __name__ == "__main__":
    app.run(debug=True)
