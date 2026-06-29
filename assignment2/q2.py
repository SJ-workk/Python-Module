password = input("Enter your password: ")

if len(password) < 6 or password.isalpha():
    print("Weak")
elif len(password) >= 8 and any(c in "@#$%&" for c in password) and any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
    print("Strong")
else:
    print("Moderate")