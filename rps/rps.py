from random import choice
comp_wins = 0
user_wins = 0
comp = ["rock", "paper", "scissors"]
you = " "
while ((you != "rock") or (you != "paper") or (you != "scissors")):
    you = input("Rock, paper or scissors?").lower()
if ((comp == "paper" and you == "scissors") or (comp == "rock" and you == "paper") or (comp == "scissors" and you == "rock")):
    print("You win!")
else:
    print("You lose")

