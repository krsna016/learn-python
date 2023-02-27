import re
regex_object = re.compile(r"bat(wo)+man")
string = "batman"
match_object = regex_object.search(string)
print(match_object == None)