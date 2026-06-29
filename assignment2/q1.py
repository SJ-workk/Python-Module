numbers = [12, 25, 35, 40, 55, 18, 30, 45]

for num in numbers:
    if num > 50:
        break
    if num % 5 == 0:
        continue
    print(num)