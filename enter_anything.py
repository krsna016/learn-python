while True:
    try:
        num = int(input("Enter the number : "))
    except ValueError:
        pass
    else:
        if(num == 0):
            break