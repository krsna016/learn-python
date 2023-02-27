nums = [1,2,3,4,5,6,7]
print("The first three items in the list are : ")
print(tuple(num for num in nums[:3]))
print("The three items from the middle are : ")
print(tuple(num for num in nums[2:5]))
print("The last three item in the list are : ")
print(tuple(num for num in nums[-3:]))