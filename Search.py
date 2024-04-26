# this is a Model class for the transportation problem
class TransportationProblem(object):
    def __init__(self, N):
        # N = number of blocks
        self.N = N
    
    def startState(self):
        return 1
    
    def isEndState(self, state):
        return state == self.N
    
    def getSuccAndCost(self, state):
        result = []
        if state + 1 <= self.N:
            result.append(('Walk',(state + 1), 1))
        if state * 2 <= self.N:
            result.append(('Tram',(state*2), 2))
        return result

# testing the model
problem = TransportationProblem(10)
print(problem.getSuccAndCost(3))
print(problem.getSuccAndCost(9))

# Algorithm Backtracking Search
def backtracking(problem):
    best= {
        'cost': float('inf'),
        'history': None
    }

    def recurse(state, history, totalcost):
        if problem.isEndState(state):
            if totalcost<best['cost']:
                best['cost'] = totalcost
                best['history'] = history
            return
        for action, nextstate, cost in problem.getSuccAndCost(state):
            recurse(nextstate, history + [action], totalcost + cost)
    recurse(problem.startState(), [], 0)
    return (best['cost'], best['history'])

print(backtracking(problem))

