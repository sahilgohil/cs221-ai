# cs221-ai

# Search Problems
Things required in a search problem,

1. State
2. Action
3. isEndState(state) -> returns true or false
4. Cost(state,action) -> returns the cost for the action on this state
5. succ(state,action) -> return the successor state using the action on this state

### Model Transportation problem
- end state
- contructor
- start state function -> returns the initial state
- isEnd function
- succandcost function -> returns the list of [action, newstate, costoftheaction]
### Backtracing Algorithm for search problem
 # requrement is that,
    - cost : any
    - time : O(b^D) 
    - space : O(b^D)
    where b is the number of actions at each state
    D is the depth of the tree

- keep track of the best solution so far
- recurse the state, keep track of the history, and total cost so far
    - check if this state is the end state
        - if it is an end state then check for if this is the best solution or not
            - if this is the best solution then change the best solution in the cache with history
    
    - recurse on the children of this state
        - for each action, newstate, cost in problem.succandcost(this state):
            recurse(newstate,history+action,totalcost+cost)

- execute the recurse function
-return the best solution

# DFS Algorithm for search problem

# requrement is that,
    - cost : 0
    - time : O(b^D) 
    - space : O(D) (no need to store the information for the previous states)
    where b is the number of actions at each state
    D is the depth of the tree
- stack is required for the DFS
- add the start state and empty history to the stack
- loop until stack is not empty
    - take out the first object from the stack
    - check if the state is an end state
        - if it is an end state then return the history for the solution
    - add the children of the state to the stack with the updated history
- return None for no solution

### BFS Algorithm for search problem

# requirement is that,
    - cost : any constant c >= 0
    - time : O(b^d) 
    - space : O(b^d)
    where b is the number of actions at each state
    d is the depth of the tree till solution is found

- make an empty queue
- add the start state and cost and history to the queue
- loop until queue is not empty
    - take out the first object from the queue
    - check if the state is an end state
        - if it is an end state then return the cost and history for the solution
    - add the children of the state to the queue with the updated history and cost
- return None for no solution

### Dynamic Programming for search problem
## Basic without any constraints
# requirement is that,
    - the dynamic programminc requries a state which is determined by us
    - the state must be sufficient for us to decide the future state optimally
    - futureCost(state) = {
                            {min(a): cost(state,a) + futureCost(succ(state,a))}
                            0      : isEndState(state)
                            }
    - requires a cache to maintain the past calculated costs

## Constraint is that cant visit 3 odd cities in a row
# now the state must have one more variable
# requirement is that,
    - must not visit 3 odd cities in a row.
    - the state will be s = (is prev city odd?, currentCity)

### Uniform Cost Search for search problem
## cost can be any
# requirement is that,
    - cost : any
    - time :
    - space :
    - has three sets 
    1. Explored: has all the area that are explored with their optimal path known
    2. Frontier: has all the area that are explored but their optimal path is unknown
    3. Unexplored: has all the area that are yet to be explored
    SUDO code is:
    - add start state to frontier (Priority Queue)
    - loop until frontier is empty
        - take out the first object from the frontier which has the smallest priority p
        - check if the state is an end state
            - return the solution
        - add the state to the explored set
        -for each action a belongs to Action(s):
            - get the successor state S'
            - if the S' is already in the explored then continue
            -update the frontier with S' with priority p+cost(s,a)
    

### A* Search for search problem
## cost can be any
# requirement is that,
    - cost : any
    - time :
    - space :
