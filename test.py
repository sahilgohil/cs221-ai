import unittest
import Search

# create a test case for backtracking algorithm
class TestBacktracking(unittest.TestCase):
    def test_backtracking(self):
        # test case for backtracking algorithm
        problem = Search.TransportationProblem(10)
        minimumCost = Search.backtracking(problem)
        self.assertEqual(minimumCost, 6)

if __name__ == '__main__':
    unittest.main()