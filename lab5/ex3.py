class Vehicle:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model} {self.color}"

class Car(Vehicle):
    def __init__(self, brand, model, color, year, engine_capacity, fuel_efficiency):
        super().__init__(brand, model, color, year)
        self.engine_capacity = engine_capacity
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

    def display_info(self):
        return f"{super().display_info()} {self.engine_capacity}"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, color, year):
        super().__init__(brand, model, color, year)

class Truck(Vehicle):
    def __init__(self, brand, model, color, year, towing_capacity):
        super().__init__(brand, model, color, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return self.towing_capacity

car = Car(brand="Dacia", model="Golan", year=2022, color="Culoare_bostan", engine_capacity="2.3", fuel_efficiency=50)
print(car.display_info())
print("Mileage for a 100km:", car.calculate_mileage(100))

motorcycle = Motorcycle(brand="Motoreta", model="Clasa1", color="rosu", year=2002)
print(motorcycle.display_info())

truck = Truck(brand="ARO", model="de_ala_bun", color="roz", year=1989, towing_capacity=5000)
print(truck.display_info())
print("Towing capacity:", truck.calculate_towing_capacity())
