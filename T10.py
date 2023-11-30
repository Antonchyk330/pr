last_digit = 6

n = 10 + last_digit
my_list = [int(input(f"Введіть {i+1}-й елемент масиву: ")) for i in range(n)]

max_element = max(my_list)
reversed_list = my_list[::-1]

print("Масив:", my_list)
print("Максимальний елемент:", max_element)
print("Масив у зворотньому порядку:", reversed_list)
