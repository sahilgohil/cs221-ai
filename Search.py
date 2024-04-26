# this is a Model class for the transportation problem
class TransportationProblem(object):
    def __init__(self, N):
        # N = number of blocks
        self.N = N
    
    # returns the start state
    def startState(self):
        return 1
    # checks if the state is an end state
    def isEndState(self, state):
        return state == self.N
    # returns the successor and cost of the state
    def getSuccAndCost(self, state):
        result = []

        # state update for the walk action
        if state + 1 <= self.N:
            result.append(('Walk',(state + 1), 1))
        # state update for the tram action
        if state * 2 <= self.N:
            result.append(('Tram',(state*2), 2))
        
        return result

# testing the model
problem = TransportationProblem(10)
print(problem.getSuccAndCost(3))
print(problem.getSuccAndCost(9))

# Algorithm Backtracking Search
def backtracking(problem):
    # cache to store the best solution
    best= {
        'cost': float('inf'),
        'history': None
    }
    # start the recursion
    def recurse(state, history, totalcost):

        # check if the current state is an end state
        if problem.isEndState(state):
            if totalcost<best['cost']:
                best['cost'] = totalcost
                best['history'] = history
            return
        # for each of the children in the search tree recurse this algo
        for action, nextstate, cost in problem.getSuccAndCost(state):
            # update the history and update the cost in every iteration
            recurse(nextstate, history + [action], totalcost + cost)
    # run the function
    recurse(problem.startState(), [], 0)
    # return the best solution
    return (best['cost'], best['history'])
    
# testing the backtracking algorithm
print(backtracking(problem))

