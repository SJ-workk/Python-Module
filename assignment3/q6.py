def to_title_case(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        new_words.append(word[0].upper() + word[1:].lower())
    return " ".join(new_words)

print(to_title_case("hello world from python"))