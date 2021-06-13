import logging

logging.basicConfig(level=logging.WARNING)


class Inventory:

    def __init__(self):
        self.quantity = dict()
        self.quantity_indicator = 50

    def updateQuantity(self, item, quantity):
        self.quantity[item] = self.quantity.get(item, 0) + quantity

    def prepare(self, drink, ingredients):
        """

        :param drink: drink to prepare :string
        :param ingredients:  name and quantity : dict : name:quantity
        :return: None
        """
        for ingredient in ingredients:  # Looping over ingredients to check if it's possible to prepare this drink
            invCount = self.quantity.get(ingredient, -1)
            if invCount == 0 or invCount == -1:
                print('{} cannot be prepared because {} is not available'.format(drink, ingredient))
                return
            elif invCount < ingredients[ingredient]:
                print('{} cannot be prepared because {} is not sufficient'.format(drink, ingredient))
                return
        for ingredient in ingredients:  # If yes, then prepare drink and reduce ingredients count.
            self.quantity[ingredient] -= ingredients[ingredient]
            if self.quantity[ \
                    ingredient] < self.quantity_indicator:  # If any ingredient is not available log for refill.
                logging.warning('{} quantity needs refill'.format(ingredient))
        print('{} is prepared'.format(drink))

    def reset(self):
        self.quantity.clear()
