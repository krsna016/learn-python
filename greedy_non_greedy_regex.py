import re

string = "HAHAHAHAHA"
regex_greedy = r'(HA){3,5}'
regex_non_greedy = r'(HA){3,5}?'
regex_object_g = re.compile(regex_greedy)
regex_object_ng = re.compile(regex_non_greedy)
print(regex_object_g.search(string).group())
print(regex_object_ng.search(string).group())

