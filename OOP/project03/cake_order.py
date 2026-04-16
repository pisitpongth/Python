from birthday_cake import BirthdayCake
from cup_cake import CupCake


def main():
    print("Birthday Cake's Details:")

    message = input("Enter a message on cake: ").strip()

    flavor = input("Enter a flavor: ").strip()

    pound = float(input("How many pound: ").strip())

    order1 = BirthdayCake(message, pound, flavor, 350)

    print(str(order1))

    print()

    print("Cup Cake's Details:")

    cupcake_flavor = input("Enter a flavor: ").strip()

    piece = int(input("How many piece: ").strip())

    order2 = CupCake(piece, cupcake_flavor, 65)

    print(str(order2))

    print()

    print(
        f"Total price = {(order1.get_unit_price() * pound) + (order2.get_unit_price() * piece)}"
    )


if __name__ == "__main__":
    main()
