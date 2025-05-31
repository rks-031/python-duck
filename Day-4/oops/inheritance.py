import csv

class Item:
    # class attributes
    pay_rate = 0.8  # The pay rate after applying a discount
    all = []  # List to store all instances of Item


    # constructor method
    def __init__(self, name: str, price: float, quantity = 0 ):
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


class Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # Call to super() to access the parent class constructor
        super().__init__(name, price, quantity)

        # Run validation checks
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero"

        # Assign to self object
        self.broken_phones = broken_phones
    
        def calculate_total_price(self):
            return self.price * self.quantity

        def __repr__(self):
            return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})"


phone1 = Phone("Redmi", 500, 5, 1)
print(phone1.calculate_total_price())

print(Item.all)
print(Phone.all)