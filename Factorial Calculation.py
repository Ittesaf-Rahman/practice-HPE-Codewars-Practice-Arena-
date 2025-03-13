number = int(input("Type an integer : "))
def factorial(number):
    if number == 0:
        print("The factorial of 0 is : 1")
    else:
        num = 1
        for i in range(1, number + 1):
            num = num * i
        print(f"The factorial of {number} is : {num}")
call = factorial(number)