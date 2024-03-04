#delete duplicate items
numbers = [1,2,3,4,1,5,6,2,7]
for num in numbers:
    i = 0
    if numbers.count(num) > 1:
        numbers.pop(i)
print(numbers)
