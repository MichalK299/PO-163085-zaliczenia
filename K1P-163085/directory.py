from file import File


class Directory(File):

    def __init__(self, name: str = None, year: int = 1970, size: int = 0, elements: list[File] = []) -> None:
        self.__name = name
        self.__year = year
        self.__size = size
        self.__elements = elements
        super().__init__(name, year, size)

    @property
    def elements(self) -> list[File]:
        return self.__elements

    @elements.setter
    def elements(self, value: list[File]) -> None:
        self.__elements = value

    def add_element(self, plik) -> None:
        self.elements.append(plik)

    def rozmiar(self) -> int:
        wynik = 0
        for x in self.elements:
            wynik += x
        return wynik

    def __repr__(self) -> str:
        return f'Nazwa: {self.name} utworzony {self.year}. Rozmiar {self.size}. Zawartosc: [{self.elements}]'

