import math

class Pizza:
    price: float
    toppings: list[str]
    diameter: float

    def __init__(self, diameter: float, toppings: list[str]) -> None:
        self.diameter = diameter
        self.toppings = toppings
        self.price = 0.005 * area + length(toppings)*2

    @staticmethod
    def area(diameter)-> float:
        if diameter <= 20:
            return math.pi*((diameter/2)^2)
        else:
            print('bledny promien')
            exit(-10)

    @property
    def diameter(self):
        return self.diameter

    @diameter.setter
    def diameter(self, value) -> None:
        if  value <= 20:
            self.diameter = value
        else:
            print('bledna srednica')
            exit(-10)

    def add_toppings(self, topping: str) -> None:
        self.toppings.append(topping)

    def __repr__(self) -> str:
        if toppings:
            return \
                f'Pizza\n' \
                f'srednica: {self.diameter}\n' \
                f'dodatki: {self.toppings}\n' \
                f'cena: {self.price}'
        else:
            return \
                f'Pizza\n' \
                f'srednica: {self.diameter}\n' \
                f'cena: {self.price}'

    def __add__(self, other):
        diameter = self.diameter + other.diameter
        toppings = self.toppings + other.toppings