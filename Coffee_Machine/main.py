import json
import sys

from coffee_machine import CoffeeMachine


def coffee_outlet(file='input.json'):
    data = open(file)
    data = json.load(data)
    coffee = CoffeeMachine(data)
    coffee.start_brewing()


if __name__ == '__main__':
    # print(sys.argv)
    coffee_outlet(sys.argv[1])
