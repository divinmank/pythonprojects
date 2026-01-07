
passw = input("Type your password.\n")
verify = input("Retype your password to verify.\n")
while (passw != verify):
    print("Didnt match!")
    passw = input("Type your password.\n")
    verify = input("Retype your password to verify.\n")
#loop through the list and change the chars. We need to find a way to change it back
list(passw)
