import re
string = "Here the roboCop"
regex = r'roBocop'
regex_object = re.compile(regex,re.IGNORECASE)
match_object = regex_object.search(string)
print(match_object.group())