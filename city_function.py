def city_functions(city,country,population=""):
    """"""
    if(not population):
        return f"{city}, {country}"
    else:
        return f"{city}, {country} - {population}"