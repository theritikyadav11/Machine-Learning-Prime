class Vehicle:
    brand = "TATA"
    model = "Nexon"


class Car(Vehicle):
    def __init__(self, seats):
        self.seats = seats


class Bike(Vehicle):
    def __init__(self, engine_cc):
        self.engine_cc = engine_cc



bullet = Bike(300)
print(bullet.brand, bullet.model, bullet.engine_cc)
