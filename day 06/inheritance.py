#class Dog:
#    def walk(self):
#        print("Walk")

#This is wrong because other class has same method
#Don't Repeat Yourself!
#class Cat:
#    def walk(self):
#        print("Walk")


#That's why we have inherintance
class Mammal:
    def walk(self):
        print("Walk")

#Python doesn't like empty class, so we have to methods or just "pass"
class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def meow(self):
        print("Miau")


dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.meow()