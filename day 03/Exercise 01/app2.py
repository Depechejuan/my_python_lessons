# print an L editing the "number" list 
# and some screwdriver on my own to print a proper L, not just with X
numbers = [1, 1, 1, 1, 5]

for slash in numbers:
    output = ''
    for count in range(slash):
        if slash < numbers[-1]:
            output += '|'
        else:
            output += "-"
    print(output)
