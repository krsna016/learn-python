import re

regex = r"^\d{1,3}(,\d{3})*$"
test_1 = "12"
test_2 = "1,234"
test_3 = "1,444,555"
regex_object = re.compile(regex)
match_object_1 = regex_object.search(test_1)
match_object_2 = regex_object.search(test_2)
match_object_3 = regex_object.search(test_3)
print(match_object_1.group())
print(match_object_2.group())
print(match_object_3.group())

