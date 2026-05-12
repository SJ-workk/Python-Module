p = input("Enter your password: ")
l = len(p)
has_alpha = any(c.isalpha() for c in p)
has_digit = any(c.isdigit() for c in p)
has_spec = any(c in "@#$%&" for c in p)

if l < 6 or not has_alpha:
    print("Password strength: Weak")
elif l >= 8 and has_digit and has_spec:
    print("Password strength: Strong")
elif l >= 6 and has_digit:
    print("Password strength: Moderate")
else:
    print("Password strength: Weak (try at least 8 characters, contains letters, numbers, and special characters @, #, $, %, &)")