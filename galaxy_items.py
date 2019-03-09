class ItemToPurchase:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class River(ItemToPurchase):
    def __init__(self):
        self.name = "river"
        self.cost = 350


class Tree(ItemToPurchase):
    def __init__(self):
        self.name = "tree"
        self.cost = 175


class CornField(ItemToPurchase):
    def __init__(self):
        self.name = "corn field"
        self.cost = 200


class Mountain(ItemToPurchase):
    def __init__(self):
        self.name = "mountain"
        self.cost = 200


class Gold(ItemToPurchase):
    def __init__(self):
        self.name = "gold"
        self.cost = 425


class Bumblebees(ItemToPurchase):
    def __init__(self):
        self.name = "bumblebees"
        self.cost = 50





