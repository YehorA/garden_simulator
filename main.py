from trees.apple_tree import AppleTree
from trees.cherry_tree import CherryTree
from trees.pear_tree import PearTree
from garden import Garden

def main():
    garden = Garden()

    print("--------------GARDEN SIMULATOR--------------")
    
    def add_apple_tree():
        try:
            age = int(input("Enter age of the Apple Tree: "))
            tree = AppleTree(age)
            garden.add_tree(tree)
            print("Apple Tree added.\n")
        except ValueError:
            print("Invalid age.\n")

    def add_cherry_tree():
        try:
            age = int(input("Enter age of the Cherry Tree: "))
            tree = CherryTree(age)
            garden.add_tree(tree)
            print("Cherry Tree added.\n")
        except ValueError:
            print("Invalid age.\n")

    def add_pear_tree():
        try:
            age = int(input("Enter age of the Pear Tree: "))
            tree = PearTree(age)
            garden.add_tree(tree)
            print("Pear Tree added.\n")
        except ValueError:
            print("Invalid age.\n")

    def show_all_trees():
        print()
        for tree in garden.trees:
            garden.show_tree(tree)
        print()

    def simulate():
        print()
        garden.simulate_season()
        print()

    actions = {
        1: add_apple_tree,
        2: add_cherry_tree,
        3: add_pear_tree,
        4: simulate,
        5: show_all_trees
    }

    while True:
        print("""
1. Add Apple Tree
2. Add Cherry Tree
3. Add Pear Tree
4. Simulate Season
5. Show All Trees
6. Exit""")
        try:
            user_input = int(input("Choose option: "))
        except ValueError:
            print("Invalid input.\n")
            continue

        if user_input == 6:
            break

        action = actions.get(user_input)
        if action:
            action()
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
