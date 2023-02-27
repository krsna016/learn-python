import re
regex = re.compile(r'[^aeiouAEIOU]')
search = 'RoboCop eats baby food. BABY FOOD.'
regex_object = re.compile(regex)
print(regex_object.findall(search))