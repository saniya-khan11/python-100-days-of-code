rock='''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
item=[rock,paper,scissor]
print(f"You chose : {item[choice]}")
import random
comp_choice =random.randint(0,2)
print(f"Computer chose: {item[comp_choice]}")
if ((choice==0 and comp_choice==2) or (choice==1 and comp_choice==0 )or (choice==2 and comp_choice==1)):
    print("You win !")
elif((comp_choice==0 and choice==2) or (comp_choice==1 and choice==0) or (comp_choice==2 and choice==1)):
    print("Computer wins !")
else:
    print("Match is tie")


