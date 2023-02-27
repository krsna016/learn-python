def modify_format(list_1):
    """ 
    Modify and printing the items in the list 
    by placing 'and' before the last item   
    """
    if not list_1:
        print("The list is Empty.")
    else:
        for item in list_1[0:len(list_1)-1]:
            print(item.title(),end=",")
        print(" and "+list_1[-1].title())
modify_format(['apples', 'bananas', 'tofu', 'cats'])
modify_format([])

