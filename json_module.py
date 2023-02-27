import json

numbers = [1,2,3,4]
file_path = "books_material + json + csv + txt + other_files/json_files/numbers.json"
with open(file_path,"w") as file_object:
    json.dump(numbers,file_object)
with open(file_path) as file_object:
    number = json.load(file_object)
print(number)