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
    def test_bfs(self):
        # test case for bfs algorithm
        problem = Search.TransportationProblem(10)
        history,cost = Search.bfs(problem)
        expectedHistory = ['Walk', 'Tram', 'Walk', 'Tram']
        expectedCost = 4
        self.assertEqual(history, expectedHistory)
        self.assertEqual(cost, expectedCost)
    def test_dp(self):

        problem = Search.TransportationProblem(10)
        solution = Search.dynamicProgramming(problem)
        expectedSolution = 6
        self.assertEqual(solution, expectedSolution)

if __name__ == '__main__':
    unittest.main()