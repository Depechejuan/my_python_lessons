numbers = [5,2,1,5,7,4]
numbers.append(20)
print(numbers)
# 1st argument is position, 2n number to add
numbers.insert(0,10)
print(numbers)

print(numbers.count(5))
print(numbers.index(5))
# print(numbers.index(50)) GENERATE ERROR!!!
print(50 in numbers)

#make an independent list, so we can modify the original 
numbers2 = numbers.copy()

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)



numbers.clear()
print(numbers)
print(numbers2)