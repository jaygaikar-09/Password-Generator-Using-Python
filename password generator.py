import string
import random


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def password_generator():
    pass_len = int(input("How Much Long Password You Need : "))
    random.shuffle(characters)

    password = []

    for i in range(pass_len):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)
    print(password)

functions = input("Do You Want To Generate A Password? (Yes/No): ")

if functions.lower() == "yes":
    password_generator()
elif functions.lower() == "no":
    print("Programm Ended")
    quit()
else:
    print("Invalid Input. Please input Yes or No")
    quit()