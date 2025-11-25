class Herbivore:
    def herb_info(self):
        print("Herbivore: Eats only plants.")

    def eat(self):
        print("Eating grass and leaves.")


class Carnivore:
    def carn_info(self):
        print("Carnivore: Eats only meat.")

    def eat(self):
        print("Eating meat.")


class Omnivore:
    def omni_info(self):
        print("Omnivore: Eats both plants and meat.")

    def eat(self):
        print("Eating both plants and meat.")


class Bear(Omnivore, Herbivore, Carnivore):
    pass


b = Bear()

b.omni_info()
b.herb_info()
b.carn_info()

b.eat()   
