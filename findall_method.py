import re
search = 'Phone numbers are : 54363-21190 and 97456-36321'
regex_0 = r'(\d{5})-(\d{5})'
regex_1  = r'\d{5}-\d{5}'
regex_object_0 = re.compile(regex_0)
regex_object_1 = re.compile(regex_1)
print(regex_object_0.findall(search))
print(regex_object_1.findall(search))
