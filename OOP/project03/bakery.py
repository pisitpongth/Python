class Bakery:
    def __init__(self, flavor="", unit_price=0):
        self.flavor = flavor
        self.unit_price = unit_price

    def get_flavor(self):
        return self.flavor

    def get_unit_price(self):
        return self.unit_price

    def __str__(self):
        return "Thank you for your order!"
