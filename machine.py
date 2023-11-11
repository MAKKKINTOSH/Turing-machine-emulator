from config import Config
from machine_modules.parser import Parser
from machine_modules.head import Head

class Machine:
    """
    Машина Тьюринга
    """

    def __init__(self, alphabet: list, states: dict):
        self.__word = None
        self.__alphabet = alphabet
        self.__alphabet.append(Config.empty_symbol)
        self.__states = Parser.parse_states(states)
        self.__state = self.__states[1]
        self.__head = Head()

    def run(self, input: str) -> str:
        """Обработкой слова машиной, возвращает результат работы"""

        self.__state = self.__states[1]
        self.__head.refresh_index()

        self.__word = Parser.parce_input(input)

        while self.__state.get_state() != 0:

            self.__check_word_limits()

            current_symbol = self.__word[self.__head.get_index()]

            symbol_to_set = self.__state.get_symbol_to_set(current_symbol)    # символ для подстановки вместо текущего
            move_direction = self.__state.get_move_direction(current_symbol)  # куда будет двигаться головка
            next_state = self.__states[self.__state.get_next_state(current_symbol)]          # следующее состояние машины

            self.__head.set_symbol(
                symbol=symbol_to_set,
                word=self.__word
            )
            self.__head.move(
                direction=move_direction
            )
            self.__state = next_state

        return ("".join(self.__word)).strip()

    def __check_word_limits(self) -> None:
        """Создает имитацию бесконечной ленты.
           Если головка приближается к границам слова, добавляет пустые символы
        """

        if self.__head.get_index() == 0:
            self.__word.insert(0, Config.empty_symbol)
            self.__head.move('r')
        elif self.__head.get_index() == len(self.__word) - 1:
            self.__word.append(Config.empty_symbol)

    def __str__(self):
        return f"Turing Machine\n" \
               f"States: {self.__states}\n" \
               f"Alphabet: {self.__alphabet}"
