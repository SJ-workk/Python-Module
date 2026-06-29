books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10
}

book_name = input("Enter the name of the book: ")

while True:
    copies_str = input("Enter number of copies you want: ")
    try:
        copies = int(copies_str)
        if copies <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if book_name in books:
    available = books[book_name]
    if available >= copies:
        print("Available")
    else:
        print("Partially Available")
else:
    print("Unavailable")