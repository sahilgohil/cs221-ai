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