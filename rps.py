import random

options = ['rock','paper','scissor']

while True:
    userchoice = input("Choose rock, paper, scissor (or 'quit' to stop playing): ").lower()
    if userchoice == 'quit':
        print("Thanks for playing")
        break
    if userchoice not in options:
        print("Enter a valid response")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if computer_choice == userchoice:
        print("Its a tie!")
    elif (userchoice == "rock" and computer_choice == 'scissor') or\
        (userchoice == "paper" and computer_choice == 'rock') or\
        (userchoice == "scissor" and computer_choice == 'paper'):
        print('You Win!!')
    else:
        print("Better luck next time")

    



 
