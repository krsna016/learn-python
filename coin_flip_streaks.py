import random
amount = int(input("Enter the amount of time you want coins flips : "))
number_of_streaks_of_6 = 0
streak = 0
random_coin_flips = []
for i in range(amount):
    collect = random.randint(0,1)
    if(collect == 0):
        random_coin_flips.append("H")
    elif(collect == 1):
        random_coin_flips.append("T")
for i in range(amount-1):
    if(random_coin_flips[i] == random_coin_flips[i+1]):
        streak += 1
    else:
        streak = 0
    if(streak == 6):
        number_of_streaks_of_6 += 1
print("Percentage of getting a streak of 6 heads or tails in\
a row :",100*(number_of_streaks_of_6/amount), "%")

