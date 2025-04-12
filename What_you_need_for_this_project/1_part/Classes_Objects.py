class Person:
    def __init__(self, name, age):
        self.name = name  # 'self' refers to the current object
        self.age = age

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Create an object
person1 = Person("Sukhdeep", 21)
person1.speak()
