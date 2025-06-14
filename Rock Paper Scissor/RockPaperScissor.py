import random

def Menu():
    print('''----------Welcome! To the Game of Rock-Paper-Scissor-----------
    Choose one of the three from below :
    Enter 1 for Rock.
    Enter 2 for Paper
    Enter 3 for Scissor.''')
    
    while True:
        Game()
        # Ask if user wants to play again
        try:
            choice = int(input('''\nEnter 1 for playing again.
Enter 2 for exiting the Game.\nYour choice: '''))
            if choice == 2:
                print("\n---------Exiting the Game--------------\n")
                break
            elif choice != 1:
                print("Invalid choice, exiting the game.")
                break
        except ValueError:
            print("Invalid input, exiting the game.")
            break
    
def Game():
    
    while True:
        try:
            userInput = int(input("Choose Your Option (1-Rock, 2-Paper, 3-Scissor): "))
            if userInput not in [1, 2, 3]:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a number.")
            
            
    computerInput = random.randint(1, 3)

    choices = {1: "Rock", 2: "Paper", 3: "Scissor"}

    print(f"\nYou chose: {choices[userInput]}")
    print(f"Computer chose: {choices[computerInput]}")
    
   
    if(computerInput == 1 and userInput == 2):
        print("\n----------You Win--------------\n")   
    elif(computerInput == 2 and userInput == 3):
        print("\n----------You Win--------------\n")
    elif(computerInput == 3 and userInput == 1):
        print("\n----------You Win--------------\n")  
    elif( computerInput == userInput):
        print("\n----------You tie to the Computer-----------\n")
    else:
        print("\n----------You Lose-----------\n")
       
                    
        
        
#Start the Game  
Menu()