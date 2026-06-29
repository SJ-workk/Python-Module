def check_file_empty(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return len(content.strip()) == 0

result = check_file_empty("q3.txt")
print(result)