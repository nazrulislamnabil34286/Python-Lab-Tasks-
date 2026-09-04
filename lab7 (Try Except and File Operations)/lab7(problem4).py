file_path = "sample.txt"

try:
    with open(file_path, "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("This file demonstrates Python file operations.\n")

    print("File written successfully.")

    with open(file_path, "r") as file:
        content = file.read()

    print("\nFile content after writing:")
    print(content)

    with open(file_path, "a") as file:
        file.write("This line was added using append mode.\n")

    print("Content appended successfully.")

    with open(file_path, "r") as file:
        content = file.read()

    print("\nFile content after appending:")
    print(content)

    new_file_path = "new_file.txt"

    try:
        with open(new_file_path, "x") as file:
            file.write("This file was created using create mode.\n")

        print("New file created successfully.")

    except FileExistsError:
        print("The file already exists.")

except FileNotFoundError:
    print("Error: The specified file or directory was not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("An unexpected error occurred:", e)