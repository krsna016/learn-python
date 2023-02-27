# import re
# string = "<To serve man> for dinner.>"
# regex = r'^<.*?>'
# print(re.compile(regex).search(string).group())

import re
string = "<To serve man> for dinner.>"
regex = r'^<.*>'
print(re.compile(regex).search(string).group())