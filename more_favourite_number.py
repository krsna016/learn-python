favourite_number = {}
for i in range(3):
    name = input("Enter your name : ")
    fav_num = input("Enter favourite numbers space seperated : ").split()
    favourite_number[name] = fav_num
for k,v in favourite_number.items():
    print(f"The favourite numbers of {k} are : ")
    for i in v:
        print(i)

