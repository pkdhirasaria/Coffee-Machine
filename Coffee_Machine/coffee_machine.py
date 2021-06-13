from inventory_manager import Inventory
from concurrent.futures import ThreadPoolExecutor


class CoffeeMachine:

    def __init__(self, data):
        self.inventory = Inventory()
        self.coffee_json = data
        self.outlet = data['machine']['outlets']['count_n']

    def start_brewing(self):
        for item, quantity in self.coffee_json['machine'][
            'total_items_quantity'].items():  # Update Inventory with quantity and items.
            self.inventory.updateQuantity(item, quantity)

        with ThreadPoolExecutor(
                max_workers=self.outlet) as executor:  # Creating ThreadPool with worker equals to outlet.
            for b in sorted(self.coffee_json['machine']['beverages'].keys()):
                ingredient = self.coffee_json['machine']['beverages'][b]
                executor.submit(self.inventory.prepare, b, ingredient)
