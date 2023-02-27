import re
string = "Agent Alice gave the secret documents to Agent Bob."
regex = r'Agent (\w)\w*'
regex_object = re.compile(regex)
print(regex_object.sub("CENSORED",string))
print(regex_object.sub(r"\1****",string))

