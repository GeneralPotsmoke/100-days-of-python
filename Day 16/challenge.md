#### Day 16: Object Oriented Programming (OOP)
**Challenge:** Create a class `Dog` that has attributes for name and age, and methods for barking and fetching.

```python
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
```


