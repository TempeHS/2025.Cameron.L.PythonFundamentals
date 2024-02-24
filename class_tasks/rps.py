def main():
    import random

    def generate_random():
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

    player_choice = input("Rock, paper or scissors?")
    computer_choice = generate_random()
    player_choice = player_choice.lower()
    match player_choice:
        case "rock":
            if computer_choice == "scissors":
                print("User wins")
            elif computer_choice == "paper":
                print("Ai wins")
            else:
                print("Tie")

        case "paper":
            if computer_choice == "scissors":
                print("Ai wins")
            elif computer_choice == "rock":
                print("User wins")
            else:
                print("Tie")
        case "scissors":
            if computer_choice == "paper":
                print("User wins")
            elif computer_choice == "rock":
                print("Ai wins")
            else:
                print("Tie")


main()
