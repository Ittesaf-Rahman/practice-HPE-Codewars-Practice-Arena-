def reverse(char):
    return char[::-1]
string = input("Type here : ")
reverse_string = reverse(string)
print(reverse_string.title())
if reverse_string == string:
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")