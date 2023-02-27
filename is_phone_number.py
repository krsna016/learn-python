# def is_phone_number(number):
#     """..."""
#     flag = 1
#     if(not len(number) == 12):
#         flag = 0
#     if(not number[0:3].isnumeric()):
#         flag = 0
#     if(not number[3] == "-"):
#         flag = 0
#     if(not number[4:7].isnumeric()):
#         flag = 0
#     if(not number[7] == "-"):
#         flag = 0
#     if(not number[8:12].isnumeric()):
#         flag = 0
#     if(flag == 1):
#         print("It's the american format phone number.")
#     else:
#         print("Not the american phone number.")


def is_phone_number(number):
    """..."""
    if(not len(number) == 12):
        return False
    if(not number[0:3].isnumeric()):
        return False
    if(not number[3] == "-"):
        return False
    if(not number[4:7].isnumeric()):
        return False
    if(not number[7] == "-"):
        return False
    if(not number[8:12].isnumeric()):
        return False
    else:
        return True
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if(is_phone_number(chunk)):
        print(chunk)
    else:
        pass
    
    