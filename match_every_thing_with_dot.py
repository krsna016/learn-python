import re
regex = r'My name : (.*), My age = (.*)'
search = 'My name : Anurag, My age = 20'
regex_object = re.compile(regex)
print(regex_object.findall(search))