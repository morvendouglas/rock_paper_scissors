from flask import render_template, request
from app import app
from models.game import Game
import random

@app.route('/game')
def index():
    return render_template("index.html")

@app.route('/game/<choice1>/<choice2>')
def user_plays(choice1, choice2):
    game1 = Game(choice1, choice2)
    result = game1.play_game()
    return render_template("browser_rps.html", result=result)

def computer_generator():
    choices = ["rock", "paper", "scissors"]
    return choices[random.randint(0,2)]

@app.route('/game/play', methods=['POST','GET'])
def generated_game():
    user_input = request.args.get('play')
    computer_generated = computer_generator()
    game1 = Game(user_input, computer_generated)
    result = game1.play_against_computer()
    return render_template("browser_rps.html", result=result)


