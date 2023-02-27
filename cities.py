cities = {
            "Guwahati" : {
                        "state" : "assam",
                        "population" : "1,155,000"},
            "Bikaner" : {
                        "state" : "rajasthan",
                        "population" : "802,000"
                        }
          }
for k,v in cities.items():
    print(f"All about {k} : ")
    for i,j in v.items():
        print(f"{i} = {j}")
    print()
