class ShoppingCart:
    def __init__(self):
        self.items = []

    def total_price(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total


cart = ShoppingCart()
cart.items.append({"name": "Apple", "price": 1.5})
cart.items.append({"name": "Bread", "price": 2.0})
cart.items.append({"name": "Milk", "price": 3.5})
cart.items.append({"name": "Eggs", "price": 4.0})
cart.items.append({"name": "Cheese", "price": 5.5})

print(cart.total_price())