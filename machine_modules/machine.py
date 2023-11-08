from .parser import Parser

class Machine:
    """
    Машина Тьюринга
    """

    def __init__(self, alphabet: list, states: dict):
        self.alphabet = alphabet,
        self.states = Parser.parse_states(states)

    def run(self, input: str) -> str:
        pass

    def __str__(self):
        pass
