current_users = ["Anurag","ram","shyam","sita","gita","KRSNA"]
new_users = ["ramesh","rohan","anurag","krsna"]
for name in current_users:
    if(name.lower() in new_users):
        print(name,", kindly change your username. Username already exist.")