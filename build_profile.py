def build_profile(**kwargs):
    """
    This function will take the key-value pair
    and print the dictionary
    """
    longest = []
    for i in kwargs:
        longest.append(len(i))
    longest = max(longest)
    for k,v in kwargs.items():
        print(f"{k.ljust(longest)} -> {v}")
build_profile(name = "Anurag",surname = "Pareek")