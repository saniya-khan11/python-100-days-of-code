import hangman_art 
import os
print(hangman_art.logo)

import random

from hangman_words import word_list
temp=0
end_of_game= False
chosen_word = random.choice(word_list)
#print(chosen_word)
lives=6
word_len=len(chosen_word)
display=[]
for i in range(word_len):
    display+="_"

#Join all the elements in the list and turn it into a String.
print(f"{' '.join(display)}")
while not end_of_game:
    
    guess=input("Guess a letter : ").lower()#input of lettter from the user
    os.system('cls')
    if guess in display:
        print(f"You have already guessed {guess}")
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])

    elif guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess},that's not in the word. You lose a life !")
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])
        if lives==0:
            break
    else:
        for position in range(word_len):
            letter=chosen_word[position]
            if letter == guess:
                display[position]=letter
                temp+=1
            #Join all the elements in the list and turn it into a String.
        if temp!=0:
            print(f"{guess} is present in the word.")
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])
        if "_" not in display:
            end_of_game=True
    
if lives==0:
    print("You Lose!")
    print(f"The word is '{chosen_word}'")
else:
    print("You Win!")
        
        