import re
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
phone_num_regex = re.compile(r"(\d{3})-(\d{3}-\d{4})")
string = "My number is 111-222-3334"
get = phone_num_regex.search(string)
print(get.group())
print("Area code = ",get.group(1))
print("Rem. num = ",get.group(2))
print(get.groups())

