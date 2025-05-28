import unittest
from trees.apple_tree import AppleTree
from trees.pear_tree import PearTree
from garden import Garden

class TestAppleTree(unittest.TestCase):
    def test_yield(self):
        tree = AppleTree(age=6)
        self.assertEqual(tree.get_yield(), 80)
    
    def test_yield_increases_before_peak(self):
    # Age 4 = 20, Age 5 = 50, Age 6 = 80
        self.assertGreater(AppleTree(6).get_yield(), AppleTree(5).get_yield())
        self.assertGreater(AppleTree(5).get_yield(), AppleTree(4).get_yield())

class TestGarden(unittest.TestCase):
    def test_simulate_season_increments_age(self):
        garden = Garden()
        apple = AppleTree(age=6)
        pear = PearTree(age=7)
        garden.add_tree(apple)
        garden.add_tree(pear)

        garden.simulate_season()

        self.assertEqual(apple.age, 7)
        self.assertEqual(pear.age, 8)


if __name__ == '__main__':
    unittest.main()
