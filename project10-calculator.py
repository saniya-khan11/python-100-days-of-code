from art_calculator import logo

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

#adding functions in dictionary and assigning them to dictionary's key
operations ={
    "+":add,
    "-": subtract,
    "*" : multiply,
    "/" : divide
 }
def calculator():
            print(logo)
            should_acumulate =True
            n1= float(input("What's the first number?: "))
            while should_acumulate:
                for symbol in operations:
                    print(symbol)
                typeOfOperation =input("Pick an operation: ")
                n2= float(input("What's the next number?: "))
                result = operations[typeOfOperation](n1,n2)
                print(f"{n1} {typeOfOperation} {n2} = {result}")
                choice=input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation.\n").lower()
                if choice=="y":
                    n1=result
                else :
                    should_acumulate =False
                    print("\n"*50)
                    calculator()
calculator()           
            

