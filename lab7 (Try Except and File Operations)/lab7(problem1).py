try:
    number = int(input("Enter a number: "))
    result = number / 0
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")