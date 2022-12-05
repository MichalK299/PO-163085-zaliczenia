from pizza import Pizza

class Slice(Pizza):
    how_many_slices: int

    def __init__(self, how_many_slices: int) -> None:
        self.how_many_slices = how_many_slices
        if( how_many_slices < 4 or how_many_slices >12 or how_many_slices%2 !=0):
            exit(-10)

    @property
    def how_many_slices(self):
        return self.how_many_slices

    @how_many_slices.setter
    def how_many_slices(self, value)->None:
        if (value < 4 or value > 12 or value % 2 != 0):
            exit(-10)
        self.how_many_slices = value

    @how_many_slices.getter
    def how_many_slices(self):
        return self.how_many_slices

    def part_price(self, ordered_slices):
        temp = ordered_slices/self.how_many_slices
        cena = self.cena * temp
        return cena

    def __repr__(self) -> str:
        if toppings:
            return \
                f'Pizza\n' \
                f'srednica: {self.diameter}\n' \
                f'dodatki: {self.toppings}\n' \
                f'cena: {self.price}\n' \
                f'kawalki: {self.how_many_slices}\n' \
                f'cena za kawalek: {self.price/self.how_many_slices}'
        else:
            return \
                f'Pizza\n' \
                f'srednica: {self.diameter}\n' \
                f'cena: {self.price}\n' \
                f'kawalki: {self.how_many_slices}\n' \
                f'cena za kawalek: {self.price / self.how_many_slices}'