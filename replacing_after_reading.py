file_path = "pcc_3e-main/python.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
store = ""
for line in lines:
    store += line
print(store)
print(store.replace("python", "C"))