import pprint
message = "It was a bright cold day in April, and the clocks were striking \
thirteen."
count_character = {}
for character in message:
    count_character.setdefault(character,0)
    count_character[character] += 1
# We can also write this : print(pprint.pformat(count_character))
pprint.pprint(count_character) 
