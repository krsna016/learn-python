def make_t_shirt(size,text):
    """
    This function will print the message telling 
    the size and the text to be printed on the t-shirt
    """
    print(f"The size of the t-shirt is : {size}")
    print(f"The text to be displayed on the t-shirt is : {text}")
make_t_shirt("LARGE","FONT") # Calling using the positional argument
make_t_shirt(text="FONT",size="LARGE") # Calling using the keyword argument
print()
def modified_t_shirt(text,size = "LARGE"):
    """
    This function will print the message telling 
    the size and the text to be printed on the t-shirt
    """
    print(f"The size of the t-shirt is : {size}")
    if (size == "LARGE" or size == "MEDIUM"):
        print(f"The text to be displayed on the t-shirt is : {text}")
    else:
        print("Will you be fit in this small t-shirt.")
modified_t_shirt("FONT")
modified_t_shirt("FONT","SMALL")

