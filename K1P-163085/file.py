from element import Element


class File(Element):
    def __init__(self, name: str = None, year: int = 1970, size: int = 0) -> None:
        if size < 0:
            size = 0

        self.__name = name
        self.__year = year
        self.__size = size
        super().__init__(name, year)

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        if self.size < 0:
            print('zalozenia nie spelnione')
        else:
            self.__size = value

    def __eq__(self, other) -> bool:
        if self.name == other.name and self.year == other.year and self.size == other.size:
            return True
        return False

    def __ne__(self, other) -> bool:
        if self.name == other.name and self.year == other.year and self.size == other.size:
            return False
        return True

    def __repr__(self) -> str:
        return f'Nazwa: {self.name} utworzony {self.year}. Rozmiar {self.size}'
