from random import randint

print("(intro message)")

lower = int(input("Choose the lower limit to guess from. "))
upper = int(input("Choose the upper limit to guess from. "))
num = randint(lower, upper)

x = int(input("Guess the number between "+str(lower)+" and "+str(upper)+". "))
while (num != x):
    print("Incorrect!")
    x = int(input("Guess the number between "+str(lower)+" and "+str(upper)+". "))
print("Correct! The number was "+str(num))