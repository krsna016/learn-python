table_data = [
            ['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']
            ]

def print_table(data):
    """The following function will print the well organised table"""
    longest_str_len = []
    for i in table_data:
        for j in i:
            longest_str_len.append(len(j))
    longest_str_len = max(longest_str_len)
    temp = 0
    for i in range(len(data[0])): # 0-4
        for j in range(len(data)): # 0-3
            print(table_data[j][temp].rjust(longest_str_len),end= "")
        temp += 1
        print()
print_table(table_data)