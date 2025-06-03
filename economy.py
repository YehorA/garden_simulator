class Economy:
    def __init__(self):
        self.balance = 0.0

    def calculate_tree_yield_income(self, tree):
        income = tree.get_yield() * tree.price_per_kg
        self.balance += income
        return income
    
    def charge_pruning_cost(self, tree):
        if tree.needs_pruning():
            pruning_fee = tree.pruning_cost
            self.balance -= pruning_fee
            return pruning_fee
        return 0