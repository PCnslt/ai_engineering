def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."
    
while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    user_choice = int(input("Please choose an operation (1 - 5):"))
    
    if user_choice==5:
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if user_choice==1:
        print(add(num1,num2))
    elif user_choice==2:
        print(substract(num1,num2))
    elif user_choice==3:
        print(multiply(num1,num2))
    elif user_choice==4:
        print(divide(num1,num2))
    else: 
        print("Please choose a valid operation.")