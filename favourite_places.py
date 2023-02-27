fav_places = {"Raju" : ["Bombay","Delhi","Kolkata"],
              "Ramesh" : ["America","Austria","Japan"]}
for k,v in fav_places.items():
    print(f"The favourite places of {k} are :")
    for i in v:
        print(i)