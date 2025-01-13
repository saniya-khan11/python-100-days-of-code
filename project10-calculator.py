def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
choice="n"
#adding functions in dictionary and assigning them to dictionary's key
operations ={
    "+":add,
    "-": subtract,
    "*" : multiply,
    "/" : divide
 }

while choice == 'y' or choice=='n':
    if choice =='n':
        n1= float(input("What's the first number?: "))
        for symbol in operations:
            print(symbol)
        typeOfOperation =input("Pick an operation: ")
        n2= float(input("What's the next number?: "))
        result = operations[typeOfOperation](n1,n2)
        print(f"{n1} {typeOfOperation} {n2} = {result}")
    elif choice == 'y':
        n1=result
        typeOfOperation=input("Pick an operation: ")
        n2= float(input("What's the next number?: "))
        result = operations[typeOfOperation](n1,n2)
        
        print(f"{n1} {typeOfOperation} {n2} = {result}")
    choice=input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation.\n").lower()

