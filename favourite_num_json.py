import json

def favourite_num():
    """"""
    fav_num = int(input("Enter your favourite number : "))
    file_path = "books_material + json + csv + txt + other_files/json_files/fav_num.json"
    with open(file_path,"w") as file_object:
        json.dump(fav_num,file_object)

def favourite_number_remembered():
    """"""
    file_path = "books_material + json + csv + txt + other_files/json_files/fav_num.json"
    try:
        with open(file_path) as file_object:
            fav_num = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return fav_num
def greet_user():
    """"""
    store = favourite_number_remembered()
    if store:
        print(f"I know your favourite number is : {store}")
    else:
        favourite_num()
    
greet_user()

