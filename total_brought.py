all_guests = {
            'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}
            }
def total_brought(guests,item):
    total_brought_item = 0
    for k,v in guests.items():
        total_brought_item += v.get(item,0)
    return(total_brought_item)

print("\n----Number of items being brought----\n")
print("Apples                      ---->   "+str(total_brought(all_guests,"apples")))
print("Pretzels                    ---->   "+str(total_brought(all_guests,"pretzels")))
print("Ham sandwitches             ---->   "+str(total_brought(all_guests,"ham sandwiches")))
print("Cups                        ---->   "+str(total_brought(all_guests,"cups")))
print("Cakes                       ---->   "+str(total_brought(all_guests,"cakes")))
print("Apple pies                  ---->   "+str(total_brought(all_guests,"apple pies")))


# item_name = input("Enter the item name to search for : ").lower()
# need = total_brought(al_gGuests,item_name)
# print(need)