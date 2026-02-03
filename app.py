from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Number Guessing Game</title>
</head>
<body style="text-align:center; margin-top:50px; font-family:Arial;">
    <h1>Guess a number between 1 and 10</h1>
    <form method="post">
        <input type="number" name="guess" min="1" max="10" required>
        <button type="submit">Submit</button>
    </form>
    {% if result %}
        <h2>{{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    global secret_number

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            if guess == secret_number:
                result = f"🎉 Correct! The number was {secret_number}. I picked a new number!"
                secret_number = random.randint(1, 10)  # Reset number
            elif guess < secret_number:
                result = "📈 Too low! Try again."
            else:
                result = "📉 Too high! Try again."
        except ValueError:
            result = "Please enter a valid number."

    return render_template_string(html_template, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
