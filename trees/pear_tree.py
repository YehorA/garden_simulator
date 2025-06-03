from .fruit_tree import FruitTree

class PearTree(FruitTree):
    
    def __init__(self, age: int):
        super().__init__(age)
        self.price_per_kg = 3.5
        self.pruning_cost = 7

    # Fruit begins around age 5, peaks 12-20, then declines
    def get_yield(self) -> float:
        disease_modifier = 1

        if self.has_disease:
            disease_modifier=0.5

        if self.age < 5:
            return 0
        elif 5 <= self.age < 12:
            return (30 + (self.age - 5) * 8)*disease_modifier
        elif 12 <= self.age <= 20:
            return 90*disease_modifier
        else:
            return (max(0, 90 - (self.age - 20) * 4))*disease_modifier

    def needs_pruning(self) -> bool:
        return self.age > 6 and self.age % 3 == 0

    def get_disease_risk(self) -> float:
        if self.age <= 10:
            return 0.04
        elif self.age <= 20:
            return 0.12
        else:
            return 0.25
