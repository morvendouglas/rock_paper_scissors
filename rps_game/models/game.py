import random
class Game():

    def __init__(self, choice1, choice2):
        self.choice1 = choice1
        self.choice2 = choice2

    def play_game(self):
        if self.choice1 == "rock" and self.choice2 == "scissors":
            return "Player 1 Wins! Rock beats Scissors"
        elif self.choice1 == "rock" and self.choice2 == "paper":
            return "Player 2 Wins! Paper beats Rock"
        elif self.choice1 == "paper" and self.choice2 == "scissors":
            return "Player 2 Wins! Scissors beats Paper"
        elif self.choice1 == "paper" and self.choice2 == "rock":
            return "Player 1 Wins! Paper beats Rock"
        elif self.choice1 == "scissors" and self.choice2 == "rock":
            return "Player 2 Wins! Rock beats Scissors"
        elif self.choice1 == "scissors" and self.choice2 == "paper":
            return "Player 1 Wins! Scissors beats Paper"
        else:
            None
            
    def play_against_computer(self):
        if self.choice1 == "rock" and self.choice2 == "scissors":
            return "You Win! Rock beats Scissors"
        elif self.choice1 == "rock" and self.choice2 == "paper":
            return "Sorry... Computer Wins! Paper beats Rock"
        elif self.choice1 == "paper" and self.choice2 == "scissors":
            return "Sorry... Computer Wins! Scissors beats Paper"
        elif self.choice1 == "paper" and self.choice2 == "rock":
            return "You Win! Paper beats Rock"
        elif self.choice1 == "scissors" and self.choice2 == "rock":
            return "Sorry... Computer Wins! Rock beats Scissors"
        elif self.choice1 == "scissors" and self.choice2 == "paper":
            return "You Win! Scissors beats Paper"
        else:
            None
