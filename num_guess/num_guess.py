from random import randint

print("(intro message)")

lower = int(input("Choose the lower limit to guess from. "))
upper = int(input("Choose the upper limit to guess from. "))
num = randint(lower, upper)
x = int(input("Guess the number between "+str(lower)+" and "+str(upper)+". "))
while (num != x):
    retry = int(input("Guess the number between "+str(lower)+" and "+str(upper)+". "))
    if (num != x):
        print("Try again!")
    else:
        print("Correct! The number was"+str(num))
        break