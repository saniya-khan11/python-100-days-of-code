from art_secret_auction import logo
def find_highest_bidder(bidders_dict):
    winner=""
    highest_bid = 0
    for key in bidders_dict:
        if (bidders_dict[key]) > highest_bid :
            highest_bid=bidders_dict[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}.") 
print(logo)
bidders={}
choice="yes"
while choice=="yes":
    name=input("What is your name?: ").lower()
    bid= int(input("What is your bid?: $").lower())
    bidders[name]=bid
    choice=input("Are ther any other bidders? Type 'yes' or 'no'.\n").lower()
    if choice=="yes":
        print("\n"*100)
    elif choice == "no":
        find_highest_bidder(bidders)
        

