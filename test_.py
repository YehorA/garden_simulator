import unittest
from trees.apple_tree import AppleTree
from trees.pear_tree import PearTree
from trees.cherry_tree import CherryTree
from garden import Garden

#TREES TESTING ------------------------------------------------------------------
class TestAppleTree(unittest.TestCase):
    def test_yield_peak(self):
        tree = AppleTree(age=6)
        self.assertEqual(tree.get_yield(), 80)
    
    def test_yield_increases_before_peak(self):
    # Age 4 = 20, Age 5 = 50, Age 6 = 80
        self.assertGreater(AppleTree(6).get_yield(), AppleTree(5).get_yield())
        self.assertGreater(AppleTree(5).get_yield(), AppleTree(4).get_yield())

class TestPearTree(unittest.TestCase):
    def test_yield_peak(self):
        tree = PearTree(age=12)
        self.assertEqual(tree.get_yield(), 90)
    
    def test_yield_increases_before_peak(self):
        self.assertGreater(PearTree(6).get_yield(), PearTree(5).get_yield())
        self.assertGreater(PearTree(8).get_yield(), PearTree(7).get_yield())

    def test_disease(self):
        tree = PearTree(age=12)
        tree.has_disease = True
        self.assertEqual(tree.get_yield(), 45)

class TestCherryTree(unittest.TestCase):
    def test_yield_peak(self):
        tree = CherryTree(age=11)
        self.assertEqual(tree.get_yield(), 80)
    
    def test_yield_increases_before_peak(self):
        self.assertGreater(CherryTree(6).get_yield(), CherryTree(5).get_yield())
        self.assertGreater(CherryTree(5).get_yield(), CherryTree(4).get_yield())
#-----------------------------------------------------------------------------

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
