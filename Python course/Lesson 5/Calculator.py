#Program make a simple calculator
#This function adds two numbers
def add(x, y):
    return x + y
#this function subtracts two numbers
def subtract(x, y):
    return x - y
#this function multiplies two numbers
def multiply(x, y):
    return x * y
#this function divides two numbers
def divide(x, y):
    return x / y
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("sum:", add(num1, num2))
print("difference:", subtract(num1, num2))
print("product:", multiply(num1, num2))
print("quotient:", divide(num1, num2))