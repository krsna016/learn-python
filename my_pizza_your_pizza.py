pizzas = ["Normal Pizza","Cheese Pizza","Mayonese Pizza"]
friends_pizzas = pizzas[:]
pizzas.append("Veg Pizza")
friends_pizzas.append("Fried Pan Pizza")
print("My favourite pizza's are : ")
for pizza in pizzas:
    print(pizza)
print()
print("My friend's favourite pizza's are : ")
for pizza in friends_pizzas:
    print(pizza)
