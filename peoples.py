person_1 = {"first_name" : "anurag","last_name" : "pareek","age" :"20"}
person_2 = {"first_name" : "krsna","last_name" : "...","age" :"20"}
person = [person_1,person_2]
for i in person:
    for k,v in i.items():
        print(f"{k} : {v}")
    print()