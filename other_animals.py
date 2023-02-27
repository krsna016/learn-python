dog = {"Kind":"Pet animal","Owner":"Rajesh"}
cat = {"Kind":"Pet animal","Owner":"Ramesh"}
animals = [dog,cat]
for i in animals:
    for k,v in i.items():
        print(f"{k} : {v}")
    print()
