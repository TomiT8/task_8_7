import pickle
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        return f"Ahoj, volám sa {self.name} a mám {self.age} rokov."

person = Person("Tomáš", 34)

with open("person.pkl", "wb") as file:
    pickle.dump(person, file)

with open("person.pkl", "rb") as file:
    loaded_person = pickle.load(file)

print(loaded_person.greeting())