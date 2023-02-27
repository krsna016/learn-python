
import pprint
file_object = open("8-Python/created.py","w")
list = [{1:"a"},{2:"b"}]
store = pprint.pformat(list)
file_object.write("need = "+store)
file_object.close()


import created
print(created.need[0])
