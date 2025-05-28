from .fruit_tree import FruitTree

class PearTree(FruitTree):
    # Fruit begins around age 5, peaks 12-20, then declines
    def get_yield(self) -> float:
        if self.age < 5:
            return 0
        elif 5 <= self.age < 12:
            return 30 + (self.age - 5) * 8
        elif 12 <= self.age <= 20:
            return 90
        else:
            return max(0, 90 - (self.age - 20) * 4)

    def needs_pruning(self) -> bool:
        return self.age > 6 and self.age % 3 == 0

    def get_disease_risk(self) -> float:
        if self.age <= 10:
            return 0.04
        elif self.age <= 20:
            return 0.12
        else:
            return 0.25
