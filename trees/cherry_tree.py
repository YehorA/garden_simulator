from .fruit_tree import FruitTree

class CherryTree(FruitTree):

    def __init__(self, age: int):
        super().__init__(age)
        self.price_per_kg = 5
        self.pruning_cost = 12.0

    def get_yield(self) -> float:
        # Fruit begins around age 4, peaks 10–15, then declines
        disease_modifier = 1

        if self.has_disease:
            disease_modifier=0.3

        if self.age < 4:
            return 0
        elif 4 <= self.age < 10:
            return (20 + (self.age - 4) * 10)*disease_modifier
        elif 10 <= self.age <= 15:
            return 80*disease_modifier
        else:
            return max(0, 80 - (self.age - 15) * 6)*disease_modifier

    def needs_pruning(self) -> bool:
        return self.age >= 6 and self.age % 2 == 0

    def get_disease_risk(self) -> float:
        if self.age <= 7:
            return 0.05
        elif self.age <= 15:
            return 0.15
        else:
            return 0.3
