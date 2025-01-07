def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
choice="n"

while choice == 'y' or choice=='n':
    if choice =='n':
        n1= float(input("What's the first number?: "))
        print("+ \n- \n* \n/")
        operation=input("Pick an operation: ")
        n2= float(input("What's the next number?: "))
        if operation == '+':
            result = add(n1,n2)
        elif operation == '-':
            result = subtract(n1,n2)
        elif operation == '*':
            result = multiply(n1,n2)
        else:
            result = divide(n1,n2)
        print(f"{n1} {operation} {n2} = {result}")
    elif choice == 'y':
        n1=result
        operation=input("Pick an operation: ")
        n2= float(input("What's the next number?: "))
        if operation == '+':
            result = add(n1,n2)
        elif operation == '-':
            result = subtract(n1,n2)
        elif operation == '*':
            result = multiply(n1,n2)
        else:
            result = divide(n1,n2)
        print(f"{n1} {operation} {n2} = {result}")
    choice=input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation.\n").lower()

