score = 0
print("Welcome to the quiz! I will ask you 5 trivia questions.")
x = input("Would you like to play?\n")
if x.lower() != "yes":
    quit()
q1 = input("Who was Robin Hood's Second in command?\n").lower().strip()
if q1 in ["little john", "john"]:
    score += 1
    print("Correct!")
else:
    print("Incorrect")

q2 = input("Homichlophobia is the fear of what?\n")
if (q2.lower() == "fog" or q2.lower() == "humidity"):
    score += 1
    print("Correct!")
else:
    print("Incorrect")

q3 = input("What was the world's first antibiotic?\n")
if (q3.lower() == "penicillin"):
    score += 1
    print("Correct")
else:
    print("Incorrect")

q4 = int(input("How many noses does a slug have? Numbers only\n"))
if (q4 == 4):
    score += 1
    print("Correct")
else:
    print("Incorrect")

q5a, q5b = input("What two colors appear on the flag of Greece? Enter your answer separated by a space.\n").split()
if ((q5a == "blue" and q5b == "white") or (q5a == "white" and q5b == "blue")):
    score += 1
    print("Correct")
else:
    print("Incorrect")
print("You got: ", score, "/5" )