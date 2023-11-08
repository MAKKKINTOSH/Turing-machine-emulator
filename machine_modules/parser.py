from .state import State


class Parser:
    """
    description
    """

    @staticmethod
    def parse_states(dict_states: dict) -> list[State]:
        """
        description
        """

        states = []
        alphabet = [i for i in dict_states.keys()]
        state_num = 1

        for key in dict_states.keys():
            rules = dict_states[key]
            state = State(state_num, alphabet, rules)
            states.append(state)
            state_num += 1

        return states
