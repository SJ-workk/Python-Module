words = ["This", "is", "good", "is"]
freq = {}

for word in words:
    w = word.lower()
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)