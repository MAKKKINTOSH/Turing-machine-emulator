from config import Config


class Head:
    """
    Класс головки машины
    """

    def __init__(self):
        self.__index = Config.start_index

    def get_index(self):
        """Возвращает индекс, на котором находится головка"""
        return self.__index

    def set_symbol(self, symbol: str, word: list[str]) -> None:
        """Ставит символ в слове по индексу головки"""

        word[self.__index] = symbol

    def move(self, direction: str) -> None:
        """Двигает головку на одну ячейку по направлению direction"""

        direction = direction.lower()
        if direction == 'l':
            self.__move_left()
        elif direction == 'r':
            self.__move_right()

    def __move_right(self) -> None:
        self.__index += 1

    def __move_left(self) -> None:
        self.__index -= 1

    def refresh_index(self) -> None:
        self.__index = Config.start_index
