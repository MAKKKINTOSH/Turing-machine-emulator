from .state import State
from config import Config


class Parser:
    """
    Класс преобразует исходные данные для эмулятора
    """

    @staticmethod
    def parse_states(dict_states: dict) -> list[State]:
        """
        Преобразует словарь состояний в удобную для машины форму
        """

        states = []
        alphabet = [i for i in dict_states.keys()]

        states.append(State(0, [], {}))

        for state_num in range(len(dict_states[Config.empty_symbol])):
            rules = {}
            for symbol in alphabet:
                rules[symbol] = dict_states[symbol][state_num]

            states.append(State(state_num + 1, alphabet, rules))

        return states

    @staticmethod
    def parce_input(input: str) -> list[str]:
        """
        Преобразует входное слово в массив символов
        """

        return list(input)