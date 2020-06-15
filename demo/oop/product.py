class Product:
    # Static variable/Class attribute
    tax_rate = 0.12

    @staticmethod  # Decorator
    def set_tax_rate(newrate):
        Product.tax_rate = newrate

    def __init__(self, name, price, qoh=0):
        # Object attributes
        self.name = name
        self.price = price
        self.qoh = qoh

    @property
    def net_price(self):
        return self.price + self.price * Product.tax_rate

    def purchase(self, qty):
        self.qoh += qty

    def sell(self, qty):
        self.qoh -= qty


Product.set_tax_rate(0.15)  # Call static method
p1 = Product("P1", 10000, 20)
# p2 = Product("P2", 4500)
# p2.purchase(10)
print(p1.net_price)


