users = ["admin","ram","shyam","sita","gita"]
for name in users:
    if(name == "admin"):
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+name.title()+", thank you for logging in again.")
        
users_1 = []
if(users_1):
    print("Hello users.")
else:
    print("We need to find some users!")