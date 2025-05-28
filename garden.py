class Garden:
    def __init__(self):
        self.trees = []

    def add_tree(self, tree):
        self.trees.append(tree)

    def simulate_season(self):
        for tree in self.trees:
            tree.age+=1
            print(f"{tree.__class__.__name__} (age {tree.age})")
            print(f"  Yield: {tree.get_yield()} kg")
            print(f"  Needs pruning: {tree.needs_pruning()}")
            print(f"  Disease risk: {tree.get_disease_risk() * 100:.1f}%")
            print()
        
        