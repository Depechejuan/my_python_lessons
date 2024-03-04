for item in 'Python':
    print(item)


for item in ['Mosh', "John", "Sarah"]:
    print(item)

for item in [1,2,3,4,5,6]:
    print(item)

# range 10 is 9 (from 0 to 9)
for item in range(10):
    print(item)

# It admits more arguments, begin, end(-1) and "step" (to pass or "jump")
for item in range(5, 10, 2):
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Our total is: {total}€")
#YT did t he same 👌