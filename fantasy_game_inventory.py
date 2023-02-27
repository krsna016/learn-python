players_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
drogon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] # The looted item get added into our inventory


def display_particular_inventory_item(item):
    """
    This function will provide the total number of items in the inventory
    """
    print("\n------------------------------------------\n")
    if (item in players_inventory):
        print(f"The total number of '{item}' are :",players_inventory[item])
    print("\n------------------------------------------\n")


def display_all_inventory_item():
    """
    This function will display all the total number of items in the inventory
    """
    total = 0
    print("The items in the inventory are : ")
    for item,amount in players_inventory.items():
        print(f"Total number of '{item}' are : {amount}")
        total += amount
    print("\nThe overall total number of items are :",total)
    print("\n------------------------------------------\n")
    

def add_to_inventory_and_looted_items(inventory,added_items):
    """
    This function will give the updated inventory
    """
    total = 0

    print("The looted items are : ")
    dict_added_items = dict.fromkeys((i for i in drogon_loot),0)
    for i in added_items:
        if(i in dict_added_items):
            dict_added_items[i] += 1
    for k,v in dict_added_items.items():
        print(f"Total {k} = {v}")
    print("\n------------------------------------------\n")
    
    for item in added_items:
        inventory.setdefault(item,0)
    for item in added_items:
        inventory[item] += 1
    

enter_item = input("Enter the item : ").lower()
display_particular_inventory_item(enter_item)
display_all_inventory_item()
add_to_inventory_and_looted_items(players_inventory,drogon_loot)
display_all_inventory_item()

