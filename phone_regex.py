import re
# phone_number_regex = r'(\d{3}|\(\d{3}\))?(\s| - |\.)\d{3}(\s| - |\.\d{4}(\s*(ext| x |ext.)\s*\d{2,5})?)'
phone_number_regex = r'''
                        (\d{3}|\(\d{3}\))?              # area code
                        (\s| - |\.)                     # seperator
                        \d{3}                           # first three digit
                        (\s| - |\.)                     # seperator
                        \d{4}                           # last four digits
                        (\s*(ext| x |ext.)\s*\d{2,5})?  # extension
                     '''
phone_num = "666-232-1111"
regex_object = re.compile(phone_number_regex,re.VERBOSE)
print(regex_object.search(phone_num).group())
