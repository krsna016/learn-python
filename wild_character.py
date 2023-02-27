import re
search = 'The cat in the hat sat on the flat mat.'
regex = r'.at'
regex_object = re.compile(regex)
print(regex_object.findall(search))