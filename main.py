from machine_modules.machine import Machine


def main():
    word = input()

    # dev version input
    alphabet = ['a', 'b']
    states = {
        'a': ["2aR", "2aR", "5aR", "4aL", "5 R", "0aN"],
        'b': ["3 R", "2aR", "5bR", "4bL", "5 R", "0bN"],
        ' ': ["0 N", "4 L", "-", "0 R", "6 N", "6 L"]
    }
    # dev version input

    machine = Machine(alphabet, states)
    result = machine.run(word)
    print(result)


if __name__ == "__main__":
    main()
