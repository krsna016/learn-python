import re
name = "Anurag Pareek and anurag"
a = re.compile(r"Anurag|anurag")
b = a.search(name)
print(b.group())
