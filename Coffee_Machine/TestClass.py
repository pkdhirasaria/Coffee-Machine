import unittest
import json

from coffee_machine import CoffeeMachine


class UnitTest(unittest.TestCase):

    def test_start_brewing(self):
        coffee_machine = CoffeeMachine(json.load(open('input.json')))
        res = coffee_machine.start_brewing()
        self.assertEqual(None, res)


if __name__ == '__main__':
    unittest.main()
