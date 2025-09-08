import random

def guess_number():
    number = random.randint(1, 20)
    guess = 0
    attempts = 0

    print("I'm thinking of a number between 1 and 20...")

    while guess != number:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(" Correct! You guessed it in", attempts, "tries.")

guess_number()
