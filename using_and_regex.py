import re
regex = r'bat(wo)?man'
string = "Here the batman and batwoman"
string_1 = "Here the ironman and batwoman"
regex_object = re.compile(regex)
search = regex_object.search(string)
search_1 = regex_object.search(string_1)
match_object = search.group()
match_object_1 = search_1.group()
print(match_object)
print(match_object_1)

