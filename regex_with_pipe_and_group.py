import re
string = "1Anurhag,2Anuska"
regex = r"\dAnu(rag|ska)"
a = re.compile(regex)
b = a.search(string)
print(b.group(1))
