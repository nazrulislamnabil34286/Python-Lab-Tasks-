numbers = [15, 25, 35, 45, 55]

try:
    index = input("Enter the index: ")

    if not index.lstrip("-").isdigit():
        raise TypeError("Index must be an integer.")

    index = int(index)
    print("Element:", numbers[index])

except IndexError:
    print("Error: Index is out of range.")

except TypeError as e:
    print("TypeError:", e)