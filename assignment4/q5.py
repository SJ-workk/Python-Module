def convert_to_uppercase(strings):
    return list(map(lambda x: x.upper(), strings))

words = ["apple", "ball", "camera"]
res = convert_to_uppercase(words)
print(res)