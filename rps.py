import random #for random
import os #for clearing screen


win = 0
lose = 0
rockUses = 0
paperUses = 0
scissorsUses = 0

while True:
    os.system('clear') #clear system garbage

    #take in user input
    user_choice = input(f"Choose your move: rock, paper, or scissors: ")
    user_choice = user_choice.lower()
    #take in computer input
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    print(f"\nYou chose: ", user_choice, " and the computer chose ", computer_choice, "!")

    #find out who wins
    if user_choice == computer_choice:
        print(f"\nThere is a tie!")
        if user_choice == "rock":
            rockUses += 1
        elif user_choice == "paper":
            paperUses += 1
        elif user_choice == "scissors":
            scissorsUses += 1

    elif user_choice == "rock":
        rockUses += 1
        if computer_choice == "paper":
            print("\nYou lose!")
            lose += 1
        elif computer_choice == "scissors":
            print("\nYou win!")
            win += 1
    elif user_choice == "paper":
        paperUses += 1
        if computer_choice == "rock":
            print("\nYou win!")
            win += 1
        elif computer_choice == "scissors":
            print("\nYou lose!")
            lose += 1
    elif user_choice == "scissors":
        scissorsUses += 1
        if computer_choice == "paper":
            print("\nYou win!")
            win += 1
        elif computer_choice == "rock":
            print("\nYou lose!")
            lose += 1

    print("\nYour current wins: ", win, " and your current losses: ", lose)
    print("\nYour current rock uses are: ", rockUses, " paper uses: ", paperUses," and scissors uses: ", scissorsUses)

    another_game = input("\nWant to play again? Type yes or no: ")
    if another_game.lower() == "no":
        break
