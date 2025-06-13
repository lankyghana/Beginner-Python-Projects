import random

print("I'm thinking of a number between 1 and 100,Can you guess what it is?")

expectation = random.randint(1,100) # Making a random of numbers from 1 to 100

while True:
        try:
            guess = int(input("Enter your guess: "))

#If the user guess falls within any of the conditions then it should print the outcome asigned to

            if guess > expectation:
                    print("Too high!")
            elif guess < expectation:
                    print("Too low!")
            elif guess == expectation:
                print(f"Congratulations! You've guessed the number.")
                break # Stops the loops when the user guesses the right number
        except ValueError:
                print("An error occurred, please try again.") #Handle value erros
