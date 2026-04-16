from bakery import Bakery


class CupCake(Bakery):
    def __init__(self, piece, flavor="", unit_price=0):
        super().__init__(flavor, unit_price)
        self.piece = piece

    def is_packing_box(self):
        if self.get_box_number() >= 1:
            return True
        return False

    def get_box_number(self):
        return self.piece // 6

    def get_bag_number(self):
        return self.piece % 6

    def __str__(self):
        box_info = f"{self.get_box_number()} Box " if self.is_packing_box() else ""

        total_price = self.get_unit_price() * self.piece

        return (
            f"{super().__str__()}\n"
            f"CupCake ({self.get_flavor()}) with {box_info}{self.get_bag_number()} Bag\n"
            f"Total price of Cup Cake = {total_price}"
        )
