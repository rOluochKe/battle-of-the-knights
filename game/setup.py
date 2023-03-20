class Knight:
    # Knight class with required attributes
    def __init__(self, code, name, position, status, item, attack, defence):
        self.code = code
        self.name = name
        self.position = position
        self.status = status
        self.item = item
        self.attack = attack
        self.defence = defence

class Item:
    # Item class with required attributes
    def __init__(self, code, name, attack, defence, value, position, holder):
        self.code = code
        self.name = name
        self.attack = attack
        self.defence = defence
        self.value = value
        self.position = position
        self.holder = holder

# Knights as instances of knight class
R = Knight('R', 'Red', [0,0], 'LIVE', None, 1, 1)
B = Knight('B', 'Blue', [7,0], 'LIVE', None, 1, 1)
G = Knight('G', 'Green', [7,7], 'LIVE', None, 1, 1)
Y = Knight('Y', 'Yellow', [0,7], 'LIVE', None, 1, 1)

# Items as instances of item class
M = Item('M', 'Magic Staff', 1, 1, 30, [5,2], None)
H = Item('H', 'Helmet', 0, 1, 10, [5,5], None)
D = Item('D', 'Dagger', 1, 0, 20, [2,5], None)
A = Item('A', 'Axe', 2, 0, 40, [2,2], None)

# Create lists of knights and items to iterate easily through their instances
knights = [R, B, G, Y]
items = [M, H, D, A]