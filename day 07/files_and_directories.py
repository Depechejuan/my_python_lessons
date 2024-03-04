from pathlib import Path

#Absolute Path
#C:\Program Files\Microsoft ...

#Relative Path
#./classes/day07/file.py


path = Path("ecommerce")
print(path.exists())

# We can create like this:
#path = Path("emails")
#print(path.mkdir())
#delete:
#print(path.rmdir())


path = Path()
for file in path.glob('*'):
    print(file)
