def city_names(city,country):
    """
    This function will return a neatly format
    of city with respected country
    """
    return f"{city.title()}, {country.title()}"
i = 0
while i<3:
    city,country = input("Enter city and country (Space seperated) : ").split()
    need = city_names(city,country)
    i += 1
    print(need)
