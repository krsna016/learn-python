flag = True
while flag:
    topping = input("Enter the topping : ")
    if(topping == "quit"):
        print("Thanks ! Wait for you to come again.")
        flag = False
    else:
        print(f"You have added '{topping}' topping.")