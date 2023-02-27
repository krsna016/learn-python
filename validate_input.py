while True:
    print("Enter your age : ",end="")
    age = input()
    if(age.isdecimal()):
        break
    else:
        print("...Please enter your age in numbers...")
        continue
while True:
    print("Enter the new password (only alphabets or numbers) : ",end="")
    password = input()
    if(password.isalnum()):
        break
    else:
        print("...Password should only contain alphabets or numbers...")
        continue
