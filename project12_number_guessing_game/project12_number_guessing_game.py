import random
import number_guessing_game_art as art
print(art.logo)

def guessing(number,chance):
    
    print("You are given ",chance," chances for guessing the number \n")
    for i in range(1,chance+1):
        print("Chance ",i)   
        guess = int(input("Guess a number : "))
        if guess == number :
            print("\nYour guess is correct!\nYou WIN")
            return
        elif guess> number:
            print("Too High.")
        else:
            print("Too Low.")
    print("\nYou Lose , The number is ",number)
        
def game():
    print("I'm thinking of a number between 1 to 100.")
    number = random.randint(1,100)
    while(True):
        print("Choose the difficulty level hard or easy! : ")
        difficulty = input().lower()
        if difficulty == "easy":
            guessing(number,5)
            return
        elif difficulty == "hard":
            guessing(number,10)
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
    

