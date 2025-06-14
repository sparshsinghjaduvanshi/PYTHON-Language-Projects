import random


def Menu():
    
    startPoint = 1
    endPoint = 0
    print("--------------Welcome to the Number Guessing Game!------------")
    print('''\n----------------Choose the level of difficulty------------
    [1] for High difficulty.
    [2] for Medium difficulty.
    [3] for Low difficulty.\n''')

    difficulty = int(input("Enter your choice : "))
   

    if(difficulty == 1):
        endPoint = 100
    elif(difficulty == 2):
        endPoint = 50
    else:
        endPoint = 10
        
    randomNumber = random.randint(startPoint,endPoint)
    Game(randomNumber)
    
    
    

def Game(randomNumber):
    
    guessCount = 0
    
    while True:   

        try: 
            guess = int(input("Guess The random number "))

            if(randomNumber < guess):
                print("Too high! try a lower one.\n")
                guessCount += 1
            elif(randomNumber > guess):
                print("Too Low! try a Higher one.\n")
                guessCount += 1
            elif(guess == randomNumber):
                guessCount += 1
                print("--------------Congratulation! you won the game -----------")
                print(f"You Guessed the random number in '{guessCount}' attempt.")
                break
          
        except ValueError:
                   print("\nPlease enter a valid integer.\n")
    
    while True:
        print('''\nEnter 1 to play again.
Enter 2 to exit the game.\n''')
        try:
            choice = int(input("Choose one of the above options: "))
            if choice == 1:
                Menu()
                break
            elif choice == 2:
                print("------ Exiting the game. Goodbye! ------")
                break
            else:
                print("Invalid choice. Enter 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")
            
#Start the Game           
Menu()

