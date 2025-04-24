import random
import number_guessing_game_art as art
print(art.logo)

def difficultGame(number):
    
    print("You are given 10 chances for guessing the number \n")
    for i in range(1,11):
        print("Chance ",i)   
        guess = int(input("\nGuess a number : "))
        if guess == number :
            print("\nYour guess is correct!\nYou WIN")
            return
        elif guess> number:
            print("Too High.\n")
        else:
            print("Too Low.\n")
    print("\nYou Lose , The number is ",number)
def easyGame(number):
    
    print("You are given 5 chances for guessing the number \n")
    for i in range(1,6):
        print("Chance ",i)   
        guess = int(input("\nGuess a number : "))
        if guess == number :
            print("\nYour guess is correct!\nYou WIN")
            return
        elif guess> number:
            print("Too High.\n")
        else:
            print("Too Low.\n")
    print("\nYou Lose , The number is ",number)

        
def game():
    print("I'm thinking of a number between 1 to 100.")
    number = random.randint(1,100)
    while(True):
        print("Choose the difficulty level hard or easy! : ")
        difficulty = input().lower()
        if difficulty == "easy":
            easyGame(number)
            return
        elif difficulty == "hard":
            difficultGame(number)
            return
        else :
            print("Invalid Choice")

     
while True :
    print("Welcome to the Number Guessing Game!")
    game()
    choice = input("Enter 'y' to play again and 'n' for exit : ").lower()
    if choice == 'y':
        print()
        continue
    else:
        break
    

