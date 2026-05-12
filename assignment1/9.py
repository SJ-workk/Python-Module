sentence = input("Enter a sentence: ")
words = sentence.split()
for i in range(len(words)):
    if i % 2 == 1:  
        words[i] = words[i][::-1]

result = " ".join(words)
print(result)