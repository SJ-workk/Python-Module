def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

write_to_file("q1.txt", "Wassup")

a = read_file_content("q1.txt")
print(a)