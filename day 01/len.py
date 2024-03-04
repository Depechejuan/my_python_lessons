course = "Python for Beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course)
# Differences between functions and method
# Method is for specifit type. like "upper"
# Function is for a general purpose , like "len"


#The index opf the "P" is 0
print(course.find('P'))
print(course.find('o'))
# We dont have a J so it serves -1
print(course.find('J'))

# start at 11 so that what's shown
print(course.find('Beginners'))

print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('beginners', 'Absolute Beginners'))
print(course.replace('P', '^Z'))


print('Python' in course)
print('python' in course)

# find returns index, in returns bool