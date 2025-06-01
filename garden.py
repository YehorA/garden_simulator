import random
from economy import Economy 

class Garden:
    def __init__(self):
        self.trees = []
        self.season = 1
        self.economy = Economy()

    def add_tree(self, tree):
        self.trees.append(tree)

    def show_tree(self, tree):
        print(f"{tree.__class__.__name__} (age {tree.age})")
        print(f"  Yield: {tree.get_yield()} kg")
        print(f"  Needs pruning: {tree.needs_pruning()}")
        print(f"  Disease risk: {tree.get_disease_risk() * 100:.1f}%")
        print(f"  Health status: {'Diseased' if tree.has_disease else 'Healthy'}")
        print()

    def simulate_season(self, disease_enabled=True):
        print(f"\n--- SEASON {self.season} ---")
        self.season += 1
        dead_trees = []
        income = 0

        for tree in self.trees:
            #Needed to fix test, so deseased trees wouldn't effect income
            if disease_enabled:
                tree.check_for_disease()
            tree.age += 1

            if tree.has_disease and random.random() < 0.2:
                print(f"{tree.__class__.__name__} (age {tree.age}) has died due to disease.")
                print()
                dead_trees.append(tree)

            elif tree.age > 30:
                print(f"{tree.__class__.__name__} (age {tree.age}) has died of old age.")
                print()
                dead_trees.append(tree)

            else:
                income += self.economy.calculate_tree_yield_income(tree)
                self.show_tree(tree)

        #remove dead tree
        for dead in dead_trees:
            self.trees.remove(dead)

        print(f"Your income during this season is {income}")
        print()
        print(f"Your balance is {self.economy.balance}")
