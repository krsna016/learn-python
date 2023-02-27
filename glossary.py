glossary = {"list" : "It's a data type in python and is mutable and ordered.",
            "tuple" : "It's a data type in python and is immutable and ordered",
            "dictionary" : "It's a data type in python and is mutable and unordered"}
# print(f"What is 'List' ?\nans:{glossary['list']}")
# print(f"What is 'tuple' ?\nans:{glossary['tuple']}")
# print(f"What is 'dictionary' ?\nans:{glossary['dictionary']}")
for k,v in glossary.items():
    print(f"{k} : {v}")