import re
search_1 = "Hello, World"
search_2 = "Its going on"

str_1 = "abc42"
str_2 = "wwewe"

s_1 = "abcdef"
s_2 = "abc123"

regex_1 = r'^(Hello)'
regex_2 = r'\d+$'
regex_3 = r'^[^0-9]+$'

regex_object_1 = re.compile(regex_1)
regex_object_2 = re.compile(regex_2)
regex_object_3 = re.compile(regex_3)

print(regex_object_1.search(search_1).group())
print(regex_object_1.search(search_2) == None)
print()
print(regex_object_2.search(str_1).group())
print(regex_object_2.search(str_2) == None)
print()
print(regex_object_3.search(s_1).group())
print(regex_object_3.search(s_2) == None)


