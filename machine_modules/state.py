class State:
    """
    Класс состояния машины
    """

    def __init__(self, number: int, alphabet: list, rules: dict):
        self.__number = number
        self.__alphabet = alphabet
        self.__rules = rules

    def get_state(self):
        """Возвращает номер текущего состояния"""
        return self.__number

    def get_rules(self):
        """Возвращает правила для этого состояния"""
        return self.__rules

    def get_next_state(self, symbol: str) -> int:
        """Возвращает следующее состояние"""
        return int(self.__rules[symbol][0])

    def get_symbol_to_set(self, symbol: str) -> str:
        """Возвращает символ для записи в ячейку"""
        return self.__rules[symbol][1]

    def get_move_direction(self, symbol: str) -> str:
        """Возвращает следующее положение головки"""
        return self.__rules[symbol][2]

    def __repr__(self):
        return f"state {self.__number}"
