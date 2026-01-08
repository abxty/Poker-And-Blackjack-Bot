# Poker & Blackjack Game Bot

A Python-based project combining a command-line game with a web-based statistics portal. Players can compete against automated bots in Poker or Blackjack via the CLI. Bots use rule-based decision logic informed by probability and expected value, simulating realistic gameplay behavior.  

Additionally, a Flask-based website allows players to:

- Register and log in to accounts
- Track game statistics, including the last 5 games
- View winners and game outcomes
- Monitor win/loss records and other performance metrics

## Features

- Play Poker and Blackjack in the command line
- Compete against multiple automated bots with probabilistic strategies
- Account registration and login through the web interface
- View recent game results and player statistics online
- Integrates CLI gameplay with a Flask-based tracking system

## Technologies Used

- Python 3
- Flask
- HTML/CSS templates
- Command-line interface (CLI)
- Algorithmic decision-making for bots

## Installation

1. Clone the repository:
git clone https://github.com/abxty/Poker-And-Blackjack-Bot.git

2. Navigate to the project folder:
cd Poker-And-Blackjack-Bot

3. Create a virtual environment:
python -m venv venv

4. Activate the environment:
Windows: venv\Scripts\activate  
macOS/Linux: source venv/bin/activate

5. Install dependencies:
pip install -r requirements.txt

6. Run the CLI game:
python main.py

7. (Optional) Run the web portal:
python app.py
Open your browser at http://127.0.0.1:5000

## Usage

- Play the CLI game and compete against bots
- Register an account on the website to track your performance
- View last 5 games, outcomes, and statistics through the web interface

## Learning Outcomes

- Algorithmic thinking and probability-based bot strategies
- Command-line game development
- Web application development with Flask
- User account management and game statistics tracking
- Integration of backend logic with a web interface

## Future Improvements

- Enhance bot intelligence with more advanced decision-making
- Improve web interface design and responsiveness
- Implement persistent game history across sessions
- Add authentication security improvements

## Author

Samuel George Loots  
Year 2 Computer Science Student · Cardiff University

[GitHub Repository](https://github.com/abxty/Poker-And-Blackjack-Bot)
