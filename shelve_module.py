import shelve
file = shelve.open("hello")
cats = ["a",'b','c']
file["cats"] = cats # Writing


print(file["cats"]) # Reading

print(list(file.keys()))
print(list(file.values()))

file.close() # Close 