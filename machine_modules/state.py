class State:
    """
    Класс состояния машины
    """

    def __init__(self, number: int, alphabet: list, rules: dict):
        self.number = number
        self.alphabet = alphabet
        self.rules = rules

    def get_next_state(self, symbol: str) -> int:
        """Возвращает следующее состояние"""
        return int(self.rules[symbol][0])

    def get_symbol_to_set(self, symbol: str) -> str:
        """Возвращает символ для записи в ячейку"""
        return self.rules[symbol][1]

    def get_move_direction(self, symbol: str, index: int) -> str:
        """Возвращает следующее положение головки"""
        return self.rules[symbol][2]

    def __str__(self):
        return f"state {self.number}"
