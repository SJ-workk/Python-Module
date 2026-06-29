def find_maximum(list1):
    max_num = list1[0]
    for num in list1:
        if num > max_num:
            max_num = num
    return max_num

print(find_maximum([10, 25, 5, 80, 30]))