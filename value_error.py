try:
    num_1 = int(input("Number 1 : "))
    num_2 = int(input("Number 2 : "))
except ValueError:
    print("Kindly, Enter the integer value.")
else:
    print(f"The sum of the numbers are : {num_1 + num_2}")

