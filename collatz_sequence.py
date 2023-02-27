def collatz(number):
    print("The collatz number is : ")
    while(number != 1):
        if(number % 2 == 0):
            number = number // 2
            print(number)
        elif(number % 2 != 0):
            number = (3 * number) + 1
            print(number)
try:
    num = int(input("Enter the number : ")) # Number should not be 0(zero)
    collatz(num)
except ValueError:
    print("Please write a integer value.")
