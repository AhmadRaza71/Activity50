string = input("Enter your own string to reverse: ")
string2 = ('')
for i in string:
    string2 = i + string2
print("\nThe original string is:", string)
print("\nThe reversed string is:", string2)