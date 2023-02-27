import re
regex = r'(\d{3}-)?\d{3}-\d{4}'
string = "The numbers are 123-212-344 and 333-2221"
regex_object = re.compile(regex)
search_regex = regex_object.search(string)
match_object = search_regex.group()
print(match_object)