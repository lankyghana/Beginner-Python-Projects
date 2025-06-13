import random

required_choices = { "r" : "rock🪨" ,  "p" : "paper📝", "s" : "scissors✂"}

def play_game():
        while True:
                human_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
                if human_choice not in required_choices:
                        print("Invalid Choice, try again")
                        continue
                
                machine_choice = random.choice(list(required_choices.keys())) #Assigns the required choices to the machine choice
                print(f"Computer chose : {required_choices[machine_choice]}")#prints the machines choice
                print(f"You chose : {required_choices[human_choice]}")#prints the humans choice

                if human_choice == machine_choice:
                        print(f"It's a tie!")
                elif (
                        human_choice == "r" and machine_choice == "s" or
                        human_choice == "p" and machine_choice == "r" or
                        human_choice == "s" and machine_choice == "p"
                ):
                        print("You won!")
                else:
                        print("You lose!")

                to_continue = input("Do you want to continue? (y/n)").lower() #Finds out if the user wants to continue

                if to_continue == "y":
                        continue
                elif to_continue == "n":
                        print("Hopes to see you again, Thanks!")
                        break #Game ends if the user choose "n"
                else:
                        print("Invalid input, exiting the game....")
                        break #Game ends if the user types anything else n/y
                
play_game()