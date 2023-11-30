list = [34, 3, 5, 56, -7, -34, 6, 12, 53, 10, 11, -12, 99, 44, 67, 1]
for i in range(20):
    if list[i] < 0:
     list[i] = abs(list[i])
print(list)
