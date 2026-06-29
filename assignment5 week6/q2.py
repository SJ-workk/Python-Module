class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def short_title(self):
        return self.title[:10]


b1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
b2 = Book("Frankenstein", "Mary Shelley")
b3 = Book("A Brief History of Time", "Stephen Hawking")

print(b1.short_title())
print(b2.short_title())
print(b3.short_title())