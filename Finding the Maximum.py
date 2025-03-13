list = [3, 7, 15, 31, 63]
if not list:
    print("None")
else:
    max = 0
    for i in list:
        if i > max:
            max = i
    print("The maximum number of the list is : ",max)