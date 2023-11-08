class Head:
    """
    Класс головки машины
    """

    def __init__(self):
        self.index = 1

    def move(self, direction: str) -> None:
        """Двигает головку на одну ячейку по направлению direction"""

        direction = direction.lower()
        if direction == 'l':
            self.__move_left()
        elif direction == 'r':
            self.__move_right()

    def __move_right(self) -> None:
        self.index += 1

    def __move_left(self) -> None:
        self.index -= 1
