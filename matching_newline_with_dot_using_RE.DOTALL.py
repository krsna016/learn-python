import re

search = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
regex = r'.*'
regex_object = re.compile(regex)
regex_object_1 = re.compile(regex,re.DOTALL)
print(regex_object.search(search).group())
print()
print(regex_object_1.search(search).group())
