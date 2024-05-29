import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Guess the number between 1 and 100!")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")

    print(f"Congratulations! You guessed the number in {attempts} attempts.")

guess_the_number() 
