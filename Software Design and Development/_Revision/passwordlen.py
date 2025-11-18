password = input("Enter your password")
while len(password) < 5 or len(password) > 5:
    print("Invalid password. Should be five characters in length.")
    password = input("Enter your password")
