import random

y = "y"
n = "n"

def guess():
        while True:
            guess = input("Guess the dice? (y/n): ").lower() #ask the user to guess and turn it to lowercase
            if guess == y:
                print(random.randint(1, 100)) #if the user types "y" print random numbers
            elif guess == n:
                print("Thank you for playing!") #if the user types "n" print "Thank you for playing" and stop.
                break
            else:
                print("Invalid guess, try again.") #Anything other than the "y/n" print invalid

guess()