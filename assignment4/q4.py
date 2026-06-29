def reverse_file_content(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    with open("reversed.txt", "w") as file:
        file.write(content[::-1])

reverse_file_content("q4.txt")
