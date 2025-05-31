import csv

class Item:
    # class attributes
    pay_rate = 0.8  # The pay rate after applying a discount
    all = []  # List to store all instances of Item


    # constructor method
    def __init__(self, name: str, price: float, quantity: int = 0 ):
        # Run validation checks
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    def apply_discount(self):
        self.price *= self.pay_rate

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('D:\\python-prac\\Day-4\\oops\\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# class methods are called on the class itself
# Item.instantiate_from_csv()
# print(Item.all)

# static methods can be called on the class or instance
print(Item.is_integer(7.0))  # True
print(Item.is_integer(7))    # True
print(Item.is_integer(7.5)) # False