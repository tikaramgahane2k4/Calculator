# Calcutor

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Select operator:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Divide")
print("5.Exit")

choice = int(input("Enter choise (1/2/3/4/5):"))

if choice == 5:
    print("Exiting calculator")

else:
    if choice <= 5:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

if choice == 1:
    print("Result:",add(num1,num2))

elif choice == 2:
    print("Result:", subtract(num1,num2))

elif choice == 3:
    print("Result:",multiply(num1,num2))

elif choice == 4:
    print("Result:",divide(num1,num2))

elif choice == 5:
    print()

else:
    print("Invalid input")


