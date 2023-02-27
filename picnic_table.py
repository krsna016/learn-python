picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
def table_format(item_dict,left_width,right_width):
    print("PICNIC ITEMS".center((left_width + right_width),"-"))
    for k,v in item_dict.items():
        print(f"{k.ljust(left_width,'.')}{str(v).rjust(right_width)}")

l_width = int(input("Enter the left width for the table : "))
r_width = int(input("Enter the right width for the table : "))
table_format(picnic_items,l_width,r_width)