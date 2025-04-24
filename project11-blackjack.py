import random
#function to calculate sum of elements in list
def listSum(ls):
    s =0
    for i in ls:
        
        s=s+i
    print("User list sum : ",s)
    return s

def whoWins(user,dealer):

    print(user)
    user_sum = listSum(user)
    dealer_sum = listSum(dealer)
    if user_sum == 21:
        print("User wins!")
        return
    elif user_sum > 21:
        print("User lose!")
        return
    else :
        while dealer_sum < 17:
            dealer.append(random.choice(cards))
            if dealer_sum > 21:
                print("user wins!")
                break




cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user=[]
dealer=[]
user = random.sample(cards,2)
dealer = random.sample(cards,2)
print("User cards : ",user,"\nDealer cards : ",dealer)
if listSum(user) == 21:
    print("User wins!")
elif listSum(dealer) == 21:
    print("User lose!")
choice="n"
print(type(user))
choice=input("Enter 'y' if you want to pick another card or else click 'n' : ").lower()
while choice == "y":
     #user.append(random.choice(cards))
     element =random.choice(cards)
     if element == 11:
         if (listSum(user) + element )< 21:
             user.append(11)
         else:
             user.append(random.choice(cards))
             whoWins(user,dealer)
     else:
         whoWins(user,dealer)
     

     


