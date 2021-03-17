import math
from collections import defaultdict, deque, Counter
FIFOQueue = deque
LIFOQueue = list

class Problem(object):
    """The abstract class for a formal problem. A new domain subclasses this,
    overriding `actions` and `results`, and perhaps other methods.
    The default heuristic is 0 and the default action cost is 1 for all states.
    When yiou create an instance of a subclass, specify `initial`, and `goal` states 
    (or give an `is_goal` method) and perhaps other keyword args for the subclass."""

    def __init__(self, initial=None, goal=None, **kwds): 
        self.__dict__.update(initial=initial, goal=goal, **kwds) 
        
    def actions(self, state):        
        raise NotImplementedError
        
    def result(self, state, action): 
        raise NotImplementedError
        
    def is_goal(self, state):        
        return state == self.goal
    
    def action_cost(self, s, a, s1): 
        return 1
    
    def h(self, node):               
        return 0
    
    def __str__(self):
        return '{}({!r}, {!r})'.format(
            type(self).__name__, self.initial, self.goal)
        
class Node:
    "A Node in a search tree."
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.__dict__.update(state=state, parent=parent, action=action, path_cost=path_cost)

    def __repr__(self): return '<{}>'.format(self.state)
    def __len__(self): return 0 if self.parent is None else (1 + len(self.parent))
    def __lt__(self, other): return self.path_cost < other.path_cost
    
    
failure = Node('failure', path_cost=math.inf) # Indicates an algorithm couldn't find a solution.
cutoff  = Node('cutoff',  path_cost=math.inf) # Indicates iterative deepening search was cut off.
    
    
def expand(problem, node):
    "Expand a node, generating the children nodes."
    s = node.state
    for action in problem.actions(s):
        s1 = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s1)
        yield Node(s1, node, action, cost)
        

def path_actions(node):
    "The sequence of actions to get to this node."
    if node.parent is None:
        return []  
    return path_actions(node.parent) + [node.action]


def path_states(node):
    "The sequence of states to get to this node."
    if node in (cutoff, failure, None): 
        return []
    return path_states(node.parent) + [node.state]

def breadth_first_search(problem):
    "Search shallowest nodes in the search tree first."
    node = Node(problem.initial)
    if problem.is_goal(problem.initial):
        return node
    frontier = FIFOQueue([node])
    reached = {problem.initial}
    while frontier:
        node = frontier.pop()
        for child in expand(problem, node):
            s = child.state
            if problem.is_goal(s):
                return child
            if s not in reached:
                reached.add(s)
                frontier.appendleft(child)
    return failure

class MCProblem(Problem):
  ## qtty: cantidad de misioneros y canibales a transportar
  def __init__(self, initial=None, goal=None, qtty=(3, 3)):
    self.initial = initial
    self.goal = goal
    self.qtty = qtty
  
  ## state: tiene la siguiente forma (D, M, C, M, C)
  def actions(self, state):
    """The actions executable in this state."""
    moves = [(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)]
    actions = []
    for mv in moves:
      valid_move = False
      if state[0] == 'D':
        lm = state[1] - mv[0] # left mision
        lc = state[2] - mv[1] # left cani
        rm = state[3] + mv[0] # right mission
        rc = state[4] + mv[1] # right cani
        if lm >= 0 and lc >= 0 and rm<= self.qtty[0] and rc <= self.qtty[1]:
          valid_move = True
      else:
        rm = state[3] - mv[0]
        rc = state[4] - mv[1]
        lm = state[1] + mv[0]
        lc = state[2] + mv[1]
        if rm >= 0 and rc >= 0 and lm <= self.qtty[0] and lc <= self.qtty[1]:
          valid_move = True
      
      if valid_move and ((lm >= lc and rm >= rc) or (lm == 0 or rm == 0)):
        actions.append(mv)

    return actions

  def result(self, state, action):
    """The state that results from executing this action in this state."""
    currstate = list(state)
    if state[0] == 'D':
      currstate[0] = 'L'
      currstate[1] -= action[0]
      currstate[2] -= action[1]
      currstate[3] += action[0]
      currstate[4] += action[1]
    else:
      currstate[0] = 'D'
      currstate[1] += action[0]
      currstate[2] += action[1]
      currstate[3] -= action[0]
      currstate[4] -= action[1]
    return tuple(currstate)

  def is_goal(self, state):
    """True if the goal level is in any one of the jugs."""
    return self.goal == state

mcproblem = MCProblem(initial=('D', 3, 3, 0, 0), goal=('L', 0, 0, 3, 3), qtty=(3, 3))
ans_node = breadth_first_search(mcproblem)
print(path_actions(ans_node))
print(path_states(ans_node))