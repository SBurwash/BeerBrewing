
class BeerElement:
    def __init__(self, type, name):
        self.Type = type
        self.Name = name
        self.Price = {}
        self.Weight = []


    def setPrice(self, weight, price):
        self.Weight.append(weight)
        self.Price[weight] = price

