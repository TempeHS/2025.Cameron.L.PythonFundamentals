import random

user_input = int(input("Level:"))
while True:
    if user_input < 0:
        print("Invalid")
        break
    if not user_input.isdigit:
        print("Invalid")
        break

while True:
    user_output = int(input("Guess:"))
    ai_guesser = random.randint(1, user_input)
    if user_output < ai_guesser:
        print("Too small!")
    elif user_output > ai_guesser:
        print("Too large!")
    elif user_output == ai_guesser:
        print("Just right!")
        break
    else:
        print("Wrong")
