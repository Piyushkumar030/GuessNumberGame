from flask import Flask, render_template, request, session
import random
import os



app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_key")

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize the jackpot and attempt count if not already set
    if "jackpot" not in session or "count" not in session:
        session['jackpot'] = random.randint(1, 100)
        session['count'] = 0

    message = ""
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])  # Try to convert the input to an integer
        except ValueError:
            message = "Please enter a valid integer!"  # If input is invalid, show an error message
            return render_template("index.html", message=message)

        session['count'] += 1
        jackpot = session.get('jackpot')

        if guess < jackpot:
            message = "Guess Higher!"
        elif guess > jackpot:
            message = "Guess Lower!"
        else:
            message = f"Congratulations! You guessed it in {session['count']} attempts!"
            # Reset the game
            session['jackpot'] = random.randint(1, 100)
            session['count'] = 0

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)  # Flask will automatically handle the port for deployment
