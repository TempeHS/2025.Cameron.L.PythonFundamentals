import random

user_input = int(input("Level:"))
while True:
    user = user_input + 1
    user_output = int(input("Guess:"))
    ai_guesser = random.randint(0, user)
    if user_output < ai_guesser:
        print("Too small!")
    elif user_output > ai_guesser:
        print("Too large!")
    elif user_output == ai_guesser:
        print("Just right!")
        break
    else:
        print("Wrong")

    if user_input or user < 0:
        print("Invalid")
