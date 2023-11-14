class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        pass

    def print_info(self):
        return f"Nume: {self.name}\nHabitat: {self.habitat}"

class Mammal(Animal):
    def __init__(self, name, habitat, color):
        super().__init__(name, habitat)
        self.color = color

    def give_birth(self):
        return f"{self.name} naste pui vii"

    def make_sound(self):
        return "Sunet de mamifer"

class Bird(Animal):
    def __init__(self, name, habitat, color):
        super().__init__(name, habitat)
        self.color = color

    def lay_eggs(self):
        return f"{self.name} lays eggs."

    def make_sound(self):
        return "Sunet de pasare(cra cra sau ceva de genu)"

class Fish(Animal):
    def __init__(self, name, habitat, color):
        super().__init__(name, habitat)
        self.color = color

    def lay_eggs(self):
        return f"{self.name} depunde oua."

    def swim(self):
        return f"{self.name} inoata."

    def make_sound(self):
        return "Sunet de peste(nu stiu daca exista asta)"


mammal = Mammal(name="leu", habitat="jungla", color="porrtocaliu")
print(mammal.print_info())
print(mammal.give_birth())
print(f"Sunet: {mammal.make_sound()}")

bird = Bird(name="vultur", habitat="munti", color="maro")
print(bird.print_info())
print(bird.lay_eggs())
print(f"Sunet: {bird.make_sound()}")

fish = Fish(name="pastrav", habitat="rau", color="argintiu")
print(fish.print_info())
print(fish.lay_eggs())
print(fish.swim())
print(f"Sunet: {fish.make_sound()}")
