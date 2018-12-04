
class BeerElement:
    def __init__(self, type, name):
        self.Type = type
        self.Name = name
        self.Price = {}
        self.weight = 0

    def setPrice(self, weight, price):
        self.Price[weight] = price

