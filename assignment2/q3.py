text = input("Enter a string: ")
words = text.split()
result = []

for i in range(len(words)):
    if i % 2 == 1:
        result.append(words[i][::-1])
    else:
        result.append(words[i])

print(" ".join(result))