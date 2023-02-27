total = 0
while True:
    age = int(input("enter your age : "))
    if(age == 0):
        break
    if(age < 3 and age > 0):
        price = 0
    elif(age >= 3 and age < 12):
        price = 10
    elif(age >= 12):
        price = 15
    total += price
print(f"The total price for the ticket is : {total}")
    
    
