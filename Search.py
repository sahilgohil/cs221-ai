import heapq
# this is a Model class for the transportation problem
class TransportationProblem(object):
    def __init__(self, N):
        # N = number of blocks
        self.N = N
    
    # returns the start state
    def startState(self):
        return 1
    # returns the state having (is previous city odd?, state)
    def startStateDP(self):
        return (False, 1)
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
    def getSuccAndCostForDP(self, state):
        result = []
        #check if the current state is odd
        isOddCurrent = state[1]%2 != 0
        isOddPrevious = state[0]
        # check for the next state
        isChecking = isOddCurrent and isOddPrevious
        
        if isChecking:
            # only add the next state if the previous state and the current state is not odd
            if state[1] + 1 % 2 ==0 and state[1]+1 <= self.N:
                result.append(('Walk',( isOddCurrent, state[1]+1 ), 1))
            if state[1] + 1 % 2 ==0 and state[1] * 2 <= self.N:
                result.append(('Tram',( isOddCurrent, state[1]*2 ), 2))
        else:
            if state[1] + 1 <= self.N:
                result.append(('Walk',( isOddCurrent, state[1]+1 ), 1))
            if state[1] * 2 <= self.N:
                result.append(('Tram',( isOddCurrent, state[1]*2 ), 2))

        return result
    # returns the successor and cost of the state for DFS
    def getSuccAndCostForDFS(self, state):
        result = []
        if state+1<=self.N:
            result.append(('Walk',state+1))
        if state*2<=self.N:
            result.append(('Tram',state*2))
        return result
    def getSuccAndCostForBFS(self, state):
        result = []

        if state+1<=self.N:
            result.append(('Walk',state+1, 1))
        if state*2<=self.N:
            result.append(('Tram',state*2, 1))
        return result

# testing the model
problem = TransportationProblem(10)
# print(problem.getSuccAndCost(3))
# print(problem.getSuccAndCost(9))

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
    return best['cost']

# Algorithm for DFS search
def dfs(problem):
    stack = []
    stack.append((problem.startState(),[]))

    while stack:
        state, history = stack.pop()
        if problem.isEndState(state):
            return history
        for action, nextstate in problem.getSuccAndCostForDFS(state):
            stack.append((nextstate, history + [action]))
    return None
def bfs(problem):
    queue = []

    queue.append((problem.startState(), [], 0))

    while queue:
        state, history, cost = queue.pop(0)
        if problem.isEndState(state):
            return (history, cost)
        for action, nextstate, actionCost in problem.getSuccAndCostForBFS(state):
            queue.append((nextstate, history + [action], cost + actionCost))
    return None

def dynamicProgramming(problem):
    cache = {}
    def futureCost(state):
        if problem.isEndState(state):
            return 0
        if state in cache:
            return cache[state]
        result = min(cost+futureCost(nextState) \
                    for action, nextState, cost in problem.getSuccAndCost(state) \
                    )
        cache[state] = result
        return result
    return futureCost(problem.startState())
# must not visit three odd cities in a row
def dpWithContraint(problem):
    cache = {}
    def futureCost(state):
        if problem.isEndState(state[1]):
            return 0
        if state in cache:
            return cache[state]
        
        result = min(cost + futureCost(nextState) \
                for action, nextState, cost in problem.getSuccAndCostForDP(state))

        cache[state] = result
        return cache[state]
    
    return futureCost(problem.startStateDP())

def compare_state(state1, state2):
    return state1[1]-state2[1]

def uniformCostSearch(problem):
    frontier = []
    explored = []
    heapq.heappush(frontier, (problem.startState(), 0))
    while frontier:
        state, pastCost = heapq.heappop(frontier)
        if problem.isEndState(state):
            return pastCost, explored
        explored = explored + [state]
        for action, nextState, cost in problem.getSuccAndCost(state):
            if nextState not in explored:
                heapq.heappush(frontier, (nextState, pastCost + cost))
    return None

    
# 1 2 3 4 5 6 7 8 9 10
# 1 3 4 5 10

# testing the backtracking algorithm
# print(backtracking(problem))
# print(dfs(problem))
# print(bfs(problem))
# print(dynamicProgramming(problem))
# print(dpWithContraint(problem))
print(uniformCostSearch(problem))
