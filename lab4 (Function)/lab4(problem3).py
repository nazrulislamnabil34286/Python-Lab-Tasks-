
def is_palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

word = input("Enter a string: ")

if is_palindrome(word):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")