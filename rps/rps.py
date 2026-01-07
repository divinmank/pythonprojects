from random import choice
comp_wins = 0
user_wins = 0
comp = ["rock", "paper", "scissors"]
you = " "
while ((you != "rock") and (you != "paper") and (you != "scissors")):
    you = input("Rock, paper or scissors?").lower()
if ((comp == "paper" and you == "scissors") or (comp == "rock" and you == "paper") or (comp == "scissors" and you == "rock")):
    print("You win!")
    user_wins += 1
else:
    print("You lose")
    comp_wins += 1

# Di
print("Your score is: "+ str(user_wins))
print("The computer's score is:", str(comp_wins))
