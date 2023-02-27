from collections import OrderedDict
dict_1 = OrderedDict()
while True:
    key = input("Key = ")
    if(key == ""):
        break
    value = input("Value = ")
    if(value == ""):
        break
    dict_1[key] = value
for k,v in dict_1.items():
    print(f"{k} : {v}")