import unittest
import Search

# create a test case for backtracking algorithm
class TestBacktracking(unittest.TestCase):
    def test_backtracking(self):
        # test case for backtracking algorithm
        problem = Search.TransportationProblem(10)
        minimumCost = Search.backtracking(problem)
        self.assertEqual(minimumCost, 6)
    def test_dfs(self):
        # test case for dfs algorithm
        problem = Search.TransportationProblem(10)
        solution = Search.dfs(problem)
        expectedSolution = ['Tram', 'Tram', 'Tram', 'Walk', 'Walk']
        self.assertEqual(solution, expectedSolution)

if __name__ == '__main__':
    unittest.main()