import sys

birthday = {"Shyam":"10 april,2002","Raghav":"9 march,2003"}

while True:
    name = input("Enter the name to access the birthday (Leave empty to exit): ").title()

    if not name:
        sys.exit()

    elif name:
        if(name in birthday):
            print("The birthdate of '"+name+"' is : "+birthday[name])

        elif(name not in birthday):
            print("The name is not in the database.")
            yes_no = input("Would you like to update the birthday for "+name+"(Y/N) : ").upper()
            if(yes_no) == "Y":
                enter_date = input("Enter the birthdate : ")
                birthday[name] = enter_date
                print()
                print("...Database Updated...")
                print()
                print("The birthdate of '"+name+"' is : "+birthday[name])
            else:
                print("Thanks. Call me again if you want any help!!")

    yes_no_2 = input("Want to search for other names (Y/N) : ").upper()
    if(yes_no_2) == "Y":
        continue
    else:
        sys.exit()
        


