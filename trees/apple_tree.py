from .fruit_tree import FruitTree

class AppleTree(FruitTree):
    
    def __init__(self, age: int):
        super().__init__(age)
        self.price_per_kg = 3.0
        self.pruning_cost = 10.0

    def get_yield(self) -> float:
        # Fruit production increases between 3 and 10 and declines after (if diseased reduced by 50%)
        disease_modifier = 1

        if self.has_disease:
            disease_modifier=0.7

        if self.age < 3:
            return 0
        elif 3 <= self.age <= 10:
            return (50 + (self.age - 3) * 10)*disease_modifier
        else:
            return max(0, 100 - (self.age - 10) * 5)*disease_modifier

    def needs_pruning(self) -> bool:
        # Needs pruning if older than 4 years
        return self.age >= 4 and self.age % 2 == 0

    def get_disease_risk(self) -> float:
        if self.age <= 5:
            return 0.05
        elif self.age <= 10:
            return 0.15
        else:
            return 0.3
