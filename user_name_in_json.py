import json

def get_stored_username():
    """"""
    file_path = "books_material + json + csv + txt + other_files/json_files/user.json"
    try:
        with open(file_path) as file_object:
            users = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return users

def get_new_user_name():
    """"""
    file_path = "books_material + json + csv + txt + other_files/json_files/user.json"
    user_name = input("Enter your name : ")
    with open(file_path,"w") as file_object:
        json.dump(user_name,file_object)
    return user_name

def greet_user():
    """"""
    need = get_stored_username()
    if need:
        print(f"Welcome back, {need}")
    else:
        need = get_new_user_name()
        print("We'll remember you when you will come back !!")

get_new_user_name()
greet_user()

