class Element:
    def __init__(self, name: str = None, year: int = 1970) -> None:
        if year > 1970 or year < 2023:
            year = 1970
        self.__name = name
        self.__year = year

    @property
    def name(self) -> str:
        return self.__name

    @property
    def year(self) -> int:
        return self.__year

    @name.setter
    def name(self, value: str) -> None:
        if self.name == '':
            print('zalozenia nie spelnione')
        else:
            self.__name = value

    @year.setter
    def year(self, value: int) -> None:
        if self.year > 1970 or self.year < 2023:
            print('zalozenia nie spelnione')
        else:
            self.__year = value

    def __repr__(self) -> str:
        return f'Nazwa: {self.name} utworzony {self.year}'

    def __eq__(self, other) -> bool:
        if self.year == other.year and self.name == other.name:
            return True
        return False

    def __ne__(self, other) -> bool:
        if self.year != other.year and self.name != other.name:
            return True
        return False

