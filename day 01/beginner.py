course = "Python's Course for Beginners"
print(course)

course2 = 'Python for "Beginners"'
print(course2)

#expands multiple lines 3 quotes
course3 = '''
Hello!

This can be used for sending emails
Thanks for reading
Juan.
'''

print(course3)



print(course[0])
print(course[1])
print(course[-1])
print(course[-2])
#excludes last one, so 3 is until 2, and stops at 3
print(course[0:3])

print(course[0:])
print(course[1:])
print(course[:5])
print(course[:])

another=course[:]


name = "Jennifer"
print(name[1:-1])
##Ennife