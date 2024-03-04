class Person:
    def name(self):
        return self
    
    def talk(self, name):
        message = "Welcome, " + name
        return message


print(Person.name("John"))
print(Person.talk("","John"))