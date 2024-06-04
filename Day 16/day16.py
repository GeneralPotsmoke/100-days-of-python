class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} is barking!"
    
    def fetch(self, item):
        return f"{self.name} fetched the {item}!"

dog = Dog("Buddy", 3)
print(dog.bark())
print(dog.fetch("ball"))
