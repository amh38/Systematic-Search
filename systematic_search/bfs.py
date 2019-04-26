from collections import deque
from search import *

def breadth_first_graph_search(problem):
    """ This implements the breadth first search strategy
        and returns the goal node """
    root = Node(problem.initial)
    if problem.goal_test(root.state):
        return root.solution()
    frontier = deque()
    frontier.append(root)
    explored = set()
    while True:
        if frontier.count == 0:
            return 0
        node = frontier.pop()
        explored.add(node)
        for action in problem.action(node.state):
            child = node.expand(problem)
            if child not in explored or child not in frontier:
                if problem.goal_test(child.state):
                    return child.solution()
                frontier.append(child)