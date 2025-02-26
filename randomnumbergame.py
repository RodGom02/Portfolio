import random

number = random.randint(1,100)
attempts = 0

while True:
    try:
        guess = int(input('Enter your guess: '))
        attempts += 1

        if guess < number:
            print('Too low, try again!')
        elif guess > number:
            print("Too high, try again")
        else:
            print(f'Congratulations!! You completed it in {attempts} tries')
            break
    except ValueError:
        print('Please enter a valid number')
        