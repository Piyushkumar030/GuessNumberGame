**Guess Number Game**

**Overview of the Project**
```
The Guess Number Game is a Python-based game where the user has to guess a randomly generated number between 1 and 100. The game provides feedback on whether the guess is higher or lower than the target number until the user guesses correctly. The number of attempts taken by the user is tracked. This project aims to entertain players and improve their number-guessing skills.

```

**Problem**

Manual guessing games or offline versions can be tedious. They often lack interactivity and feedback, making the experience less engaging for players.

**Challenges**

Maintaining player engagement, providing real-time feedback, and tracking user performance can be complex when creating a web-based version of such games.

**Solution**

The Guess Number Game solves this by providing a web-based interface, where users can easily interact with the game, get real-time feedback, and have an engaging experience on any device with a browser.

**Features**

- Number Guessing Game: The player guesses a number between 1 and 100.
- Real-time Feedback: Feedback is provided if the guess is too high or too low.
- Attempts Tracking: The game tracks the number of attempts made to guess the number correctly.
- Web Interface: A user-friendly web interface to play the game from any browser.

**Technologies Used**

- Flask: A Python web framework used to develop the web application.
- Install with: pip install flask
- HTML/CSS: Used to create the structure and style of the web interface.
- JavaScript: Handles dynamic interactions like feedback display on the page.
- Bootstrap: Used for responsive design and modern UI components.

Install with: Add the Bootstrap CDN in HTML or download locally.

**Installation Guide**
Follow these steps to run the project on your local machine:

1.  Clone the Repository
bash```
git clone https://github.com/yourusername/GuessNumberGame.git
cd GuessNumberGame
```
2. Install Required Packages
Ensure Python is installed on your system, then install the necessary dependencies using the command:

bash
```
pip install -r requirements.txt
```

3. Run the Application
Run the Flask application:

bash
```
python app.py
The application will be accessible at http://127.0.0.1:5000.
```

**Working**

1. Play the Game
- Open the web interface in your browser at http://127.0.0.1:5000.
- Click on the "Play" button to start the game.
- Guess a number between 1 and 100 and get feedback whether the guess is too high or too low.
- The game tracks the number of attempts and tells you when you've guessed correctly.

**Directory Structure**
```
GuessNumberGame/
├── app.py                         # Flask application that runs the game logic and web interface
├── static/                         # Folder for static files like CSS and JavaScript
│   ├── style.css                  # Custom styles for the game interface
│   └── script.js                  # JavaScript code for dynamic interactions
├── templates/                      # Folder for HTML templates
│   └── index.html                 # Main HTML file for displaying the game UI
├── requirements.txt               # File that lists all dependencies
├── README.md                      # This guidance file
└── download.jpeg                  # Background image for the game
└── Proctfile                      # For running website on Render

**Contributing**
Feel free to fork the repository and submit a pull request for any changes, improvements, or bug fixes. Contributions are always welcome!

**Acknowledgments**
Special thanks to the following:

- Flask for providing the web framework.
- Bootstrap for a responsive and modern UI.
- Python for making this game interactive and easy to develop.

**For any questions or issues, feel free to contact [deypiyushkumar2004@gmail.com] [https://github.com/Piyushkumar030**