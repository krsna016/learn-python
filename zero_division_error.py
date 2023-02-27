num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
try:
    div = num_1/num_2
    print(div)
except ZeroDivisionError:
    print("You can't divide a number by zero")

