numbers = []
print("Enter numbers one by one. Type -1 to stop.")
while True:
    value = int(input("Enter a number: "))  
    if value == -1:
        break
    if value > 50:
        break
            
    numbers.append(value)

print("\nOutput:")
for num in numbers:
    if num % 5 != 0:
        print(num)