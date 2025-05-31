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

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)  # Print all instances of Item
for instance in Item.all:
    print(instance.name)


# print(Item.pay_rate)  # Accessing class attribute
# print(item1.pay_rate)  # Accessing class attribute through instance

"""""
print(Item.__dict__)  # Print the attributes of the Item class
print('\n')
print(item1.__dict__)  # Print the attributes of item1 instance
"""

# item1.apply_discount()  # Apply discount to item1
# print(item1.price)

# item2.pay_rate = 0.7  # Change pay rate for item2
# item2.apply_discount()  # Apply discount to item2
# print(item2.price)








