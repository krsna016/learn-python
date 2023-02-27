magicians = ["Shyam","Ram","Sita","Gita"]


def show_magicians(magician):
    """
    This function will show the name of every magician
    """
    for name in magician:
        print("- ",name)


def the_great_magicians(magician):
    """
    The function will show the name of each magicians
    with 'the great' as prefix 
    """
    for index,name in enumerate(magician):
        magician[index] += ", the great"
        print(magician[index])


def greet_magician(magician):
    """
    This function will greet each magician with a message
    """
    for name in magician:
        print("Nice to meet you,",name,"!")


# show_magicians(magicians) # Passing a list as an argument
# the_great_magicians(magicians) # This function will change the list in place
# print(magicians) # The passed list have been changed
# print()
show_magicians(magicians) # Passing a list as an argument
the_great_magicians(magicians[:]) # This function will not change the list in place
print(magicians) # The passed list have not changed