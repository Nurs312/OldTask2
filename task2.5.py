numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
new_number = numbers.pop()
numbers.insert(0,new_number)
new = numbers.remove(1)
numbers.insert(-1,new)
print(numbers)
