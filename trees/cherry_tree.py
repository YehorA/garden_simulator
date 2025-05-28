from .fruit_tree import FruitTree

class CherryTree(FruitTree):
    def get_yield(self) -> float:
        # Fruit begins around age 4, peaks 10–15, then declines
        if self.age < 4:
            return 0
        elif 4 <= self.age < 10:
            return 20 + (self.age - 4) * 10
        elif 10 <= self.age <= 15:
            return 80
        else:
            return max(0, 80 - (self.age - 15) * 6)

    def needs_pruning(self) -> bool:
        return self.age >= 6 and self.age % 2 == 0

    def get_disease_risk(self) -> float:
        if self.age <= 7:
            return 0.05
        elif self.age <= 15:
            return 0.15
        else:
            return 0.3
