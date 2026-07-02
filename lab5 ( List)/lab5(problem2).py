
p = input("Enter a string: ")

p = p.lower()

if p == p[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")