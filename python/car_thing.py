from datetime import date

"""
Build three classes, two of which must inherit from the first 
and employ polymorphism. Between the three classes, there must 
be at least 5 methods, 3 instance attributes, 1 class attribute, 
and the parent class should have a dunder init. If you want 
you can add dunder str and dunder repr to each class.
"""


class Vehicle:
    def __init__(self, year, make, model, car_or_truck):
        self.year = year
        self.make = make
        self.model = model
        self.car_or_truck = car_or_truck

    def vehicle_identifier(self):
        print(f'This {self.car_or_truck} is a {self.year} {self.make} {self.model}.')

    def vintage_identifier(self):
        current_year = int(date.today().strftime("%Y"))
        if (current_year - self.year) > 25:
            print(f'This {self.car_or_truck} is an antique! Be careful with it!')
        elif (current_year - self.year) > 15:
            print(f'This {self.car_or_truck} is a classic! Please change the oil!')
        else:
            print(f'Wow, Mr. Moneybags, this {self.car_or_truck} is practically new!')

    def colorizer(self, color):
        print(f"Wow, I was worried this wouldn't work, but the {self.make} {self.model} looks really good in {color}!")


class Car(Vehicle):

    def __init__(self, year, make, model, car_or_truck, engine_size):
        super().__init__(year, make, model, car_or_truck)
        self.engine_size = engine_size

    def category(self):
        category = ''
        if self.engine_size == 'v4':
            category = 'boring'
        elif self.engine_size == 'v6':
            category = 'pony'
        else:
            category = 'muscle'
        print(f'The {self.make} {self.model} is a {category} car.')


class Truck(Vehicle):
    def __init__(self, year, make, model, car_or_truck, long_bed):
        super().__init__(year, make, model, car_or_truck)
        self.long_bed = long_bed

    def parking_space(self):
        if self.long_bed == True:
            print(f"This {self.make} {self.model} has a long bed and won't fit in the space!")
        else:
            print(f"This {self.make} {self.model} has a regular size bed and will park easy!")

    


car_1 = Car(2005, 'Toyota', 'Corolla', 'car', 'v4')
car_2 = Car(1990, 'Ford', 'Mustang', 'car', 'v8')

truck_1 = Truck(1990, 'Toyota', 'Tundra', 'truck', True)

print(car_1.model)
print(car_2.model)
truck_1.vintage_identifier()
car_1.colorizer('purple')
