class Product:
    def __init__(self, name, price, qoh=0):
        self.name = name
        self.price = price
        self.qoh = qoh

    def get_net_price(self):
        return self.price + self.price * 0.12

    def purchase(self, qty):
        self.qoh += qty

    def sell(self, qty):
        self.qoh -= qty


p1 = Product("P1", 10000, 20)
p2 = Product("P2", 4500)
p2.purchase(10)
print(p2.get_net_price())

print(p1.name, p1.price, p1.qoh)
