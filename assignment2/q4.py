words = ["apple", "banana", "apple", "orange", "banana", "banana"]
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

duplicates = {k: v for k, v in freq.items() if v > 1}
print(duplicates)