# import sys
# def get_formatted_name(first_name_1,last_name_1 = "",middle_name_1 = ' '):
#     """
#     This function will return a neatly formatted 
#     full name having middle_name argument as optional
#     """
#     if(middle_name_1 == " "):
#         full_name = first_name_1 + middle_name_1 + last_name_1
#     else:
#         full_name = first_name_1 + " " + middle_name_1 + " " + last_name_1
#     return f"----> Welcome, {full_name.title()}"
# name = input("Enter your name : ").split(" ")
# flag = 0
# if(len(name) == 1 and name[0].isalpha()):
#     first_name = name[0]
#     flag = 1
# elif(len(name) == 2 and name[0].isalpha() and name[1].isalpha()):
#     first_name = name[0]
#     last_name = name[1]
#     flag = 2
# elif(len(name) == 3 and name[0].isalpha() and name[1].isalpha() and name[2].isalpha()):
#     first_name = name[0]
#     middle_name = name[1]
#     last_name = name[2]
#     flag = 3
# else:
#         print("...No valid arguments for the function...")
#         sys.exit()
# if(flag == 1):
#     store = get_formatted_name(first_name_1 = first_name)
# elif(flag == 2):
#     store = get_formatted_name(first_name_1 = first_name, last_name_1 = last_name)
# elif(flag == 3):
#     store = get_formatted_name(first_name_1 = first_name, middle_name_1 = middle_name, last_name_1 = last_name)
# print(store)


def get_formatted_name(first_name,last_name,middle_name=""):
    """"""
    if(middle_name):
        return(f"{first_name} {middle_name} {last_name}")
    else:
        return(f"{first_name} {last_name}")

