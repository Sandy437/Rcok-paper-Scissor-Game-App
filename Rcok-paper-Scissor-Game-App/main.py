from flask import Flask, request, jsonify, send_from_directory
from random import choice

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data["choice"].lower()
    if user_choice not in choices:
        return jsonify(message="Invalid choice! Choose rock, paper, or scissors."), 400

    computer_choice = choice(choices)
    result = determine_winner(user_choice, computer_choice)

    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    })

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)