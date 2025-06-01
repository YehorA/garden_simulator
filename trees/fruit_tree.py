import random
from abc import ABC, abstractmethod

class FruitTree(ABC):
    def __init__(self, age: int):
        self.age = age  
        self.has_disease = False
        self.price_per_kg = None

    def check_for_disease(self):
        chance = self.get_disease_risk()
        self.has_disease = random.random() < chance

    @abstractmethod
    def get_yield(self) -> float:

        pass 

    @abstractmethod
    def needs_pruning(self) -> bool:

        pass

    @abstractmethod
    def get_disease_risk(self) -> float:

        pass
