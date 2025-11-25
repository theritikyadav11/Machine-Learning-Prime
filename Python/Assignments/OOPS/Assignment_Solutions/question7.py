class Person:
    def __init__(self,name,age=10,address="India"):
        self.name = name
        self.age = age
        self.address = address

p1 = Person("Arvind")
print(p1.name, p1.address, p1.age)
p2 = Person("Ritik",23)
print(p2.name, p2.age, p2.address)
p3 = Person("Ayush",16,"Bihar")
print(p3.name, p3.age, p3.address)