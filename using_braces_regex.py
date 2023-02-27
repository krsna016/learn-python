import re
regex_1 = r"(ha){3}"
regex_2 = r"(ha){2,5}"
str = "haha"
regex_object_1 = re.compile(regex_1)
regex_object_2 = re.compile(regex_2)
print(regex_object_1.search(str)==None)
print(regex_object_2.search(str).group())

