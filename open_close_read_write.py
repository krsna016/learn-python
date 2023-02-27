file_object = open("8-Python/a.txt","w")
file_object.write("Hello")


file_object = open("8-Python/a.txt")
print(file_object.read())

file_object.close()