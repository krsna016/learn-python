import re
regex_object = re.compile(r"bat(wo)*man")
string = "batwowowowowowoman"
search_match = regex_object.search(string)
print(search_match.group())