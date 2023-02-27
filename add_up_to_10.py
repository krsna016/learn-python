def add_up_to_ten(number):
    """"""
    sum = 0
    numbers = list(number)
    for i in numbers:
        sum += int(i)
    if(sum == 10):
        return (int(number))
    else:
        raise Exception("The digits must add up to 10")