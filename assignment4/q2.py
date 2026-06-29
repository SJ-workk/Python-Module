def find_longest_word(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    words = content.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

result = find_longest_word("q2.txt")
print(result)