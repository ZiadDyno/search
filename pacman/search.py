# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import time

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    stack = Stack()
    visited = set()

    # Push start node: (state, actions)
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        state, actions = stack.pop()

        if state in visited:
            continue
        visited.add(state)

        # Check for goal
        if problem.isGoalState(state):
            return actions

        # Add successors
        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, actions + [action]))

    return []  # if no solution found
    # util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    queue = Queue()
    visited = set()

    queue.push((problem.getStartState(), []))

    while not queue.isEmpty():
        state, actions = queue.pop()

        if state in visited:
            continue
        visited.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                queue.push((successor, actions + [action]))

    return []
    # util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

    pq = PriorityQueue()
    visited = {}
    start = problem.getStartState()

    # Push tuple: (state, actions, totalCost)
    pq.push((start, [], 0), 0)

    while not pq.isEmpty():
        state, actions, cost = pq.pop()

        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost

        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):
            newCost = cost + stepCost
            pq.push((successor, actions + [action], newCost), newCost)

    return []
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

    pq = PriorityQueue()
    start = problem.getStartState()

    # priority = g + h
    pq.push((start, [], 0), heuristic(start, problem))

    visited = {}   # state → best g-cost so far

    while not pq.isEmpty():
        state, path, g_cost = pq.pop()

        # Goal reached
        if problem.isGoalState(state):
            return path

        # Expand only if this g-cost is better than before
        if state not in visited or g_cost < visited[state]:
            visited[state] = g_cost

            for successor, action, step_cost in problem.getSuccessors(state):
                new_g = g_cost + step_cost
                priority = new_g + heuristic(successor, problem) # F-Cost

                pq.push((successor, path + [action], new_g), priority)

    return []
    #util.raiseNotDefined()


def depth_limited_dfs(problem: SearchProblem, limit: int):
    """
    Depth-limited DFS used by iterative deepening.

    Returns a tuple of (path, found, expanded) where expanded counts node
    expansions during this limited search.
    """
    from util import Stack

    # Treat None as unbounded for convenience when passed from CLI.
    depth_cap = float('inf') if limit is None else int(limit)

    stack = Stack()
    stack.push((problem.getStartState(), [], 0))
    visited = {}
    expanded = 0

    while not stack.isEmpty():
        state, path, depth = stack.pop()

        if problem.isGoalState(state):
            return path, True, expanded

        if depth >= depth_cap:
            continue

        if state in visited and visited[state] <= depth:
            continue
        visited[state] = depth

        successors = problem.getSuccessors(state)
        expanded += 1
        for successor, action, step_cost in successors:
            stack.push((successor, path + [action], depth + 1))

    return [], False, expanded


def depthLimitedSearch(problem: SearchProblem, max_depth: int = 1000):
    """
    Depth-limited DFS that mirrors CLI usage: returns only the action path and
    prints basic metrics. Uses `max_depth` to align with SearchAgent's parsing.
    """
    try:
        depth_cap = int(max_depth) if max_depth is not None else None
    except (TypeError, ValueError):
        raise AttributeError('max_depth must be an integer or None')

    start_time = time.time()
    path, found, expanded = depth_limited_dfs(problem, depth_cap)
    elapsed = time.time() - start_time

    cap_label = depth_cap if depth_cap is not None else 'inf'
    if found:
        print(f"[DLDFS] solution within depth {cap_label} | expanded {expanded} nodes | {elapsed:.4f}s")
        return path
    print(f"[DLDFS] no solution within depth {cap_label} | expanded {expanded} nodes | {elapsed:.4f}s")
    return []


def iterativeDeepeningSearch(problem: SearchProblem, max_depth: int = 1000):
    """
    Iterative deepening DFS: increase the depth limit until a path is found or
    max_depth is reached. Prints basic metrics for manual comparison.
    """
    try:
        max_depth = int(max_depth) if max_depth is not None else None
    except (TypeError, ValueError):
        raise AttributeError('max_depth must be an integer or None')

    total_expanded = 0
    start_time = time.time()

    depth = 1
    while True:
        path, found, expanded = depth_limited_dfs(problem, depth)
        total_expanded += expanded

        if found:
            elapsed = time.time() - start_time
            print(f"[IDDFS] solution at depth {depth} | expanded {total_expanded} nodes | {elapsed:.4f}s")
            return path
        if max_depth is not None and depth >= max_depth:
            print(f"[IDDFS] no solution within depth {max_depth} | expanded {total_expanded} nodes")
            return []
        depth += 1

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
iddfs = iterativeDeepeningSearch
dldfs = depthLimitedSearch
