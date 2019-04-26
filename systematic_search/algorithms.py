from collections import deque
from search import *
from priority_queue import PriorityQueue
from heapq import heappop, heapify, heappush


def breadth_first_graph_search(problem):
    """ This implements the breadth first search strategy
        and returns the goal node """
    root = Node(problem.initial)
    if problem.goal_test(root.state):
        return root
    frontier = deque()
    frontier.append(root)
    explored = set()
    while True:
        if frontier.count == 0:
            return 0
        node = frontier.popleft()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            if child.state not in explored:
                print(child.state + " > ")
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)

def deapth_first_graph_search(problem):
    root = Node(problem.initial)
    if problem.goal_test(root.state):
        return root.solution()
    frontier = list()
    frontier.append(root)
    explored = set()

    while len(frontier) > 0:
        node = frontier.pop()
        print(node.state + " > ")
        if node.state not in explored:
            if problem.goal_test(node.state):
                return node
            explored.add(node.state)
            for child in node.expand(problem):
                frontier.append(child)

def deapth_limited_graph_search_v2(problem, limit):
    root = Node(problem.initial)
    if problem.goal_test(root.state):
        return root.solution()
    frontier = list()
    frontier.append(root)
    explored = set()

    while len(frontier) > 0:
        if limit > 0:
            node = frontier.pop()
            print(node.state + " > ")
            if node.state not in explored:
                if problem.goal_test(node.state):
                    return node
                explored.add(node.state)
                for child in node.expand(problem):
                    frontier.append(child)
                limit -= 1
        else:
            return "cutoff"
    return "failure"


def deapth_limited_graph_search(problem, limit):
    return recursive_dls(Node(problem.initial), problem, limit)

def recursive_dls(node, problem, limit):
    if problem.goal_test(node.state):
        return node
    elif limit == 0:
        return "cutoff"
    else:
        cutoff_occured = False
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            # childs = node.expand(problem)
            # child = None
            # for i in range(len(childs)-1):
            #     if childs[i] != node.parent:
            #         child = childs[i]
            result = recursive_dls(child, problem, limit - 1)
            if result == "cutoff":
                cutoff_occured = True
            elif result != "failure":
                return result
        if cutoff_occured:
            return "cutoff"
        else:
            return "failure"

def iterative_deepening_search(problem, level):
    """ This implements the breadth first search strategy
        and returns the goal node """
    root = Node(problem.initial)
    if problem.goal_test(root.state):
        return root
    frontier = deque()
    frontier.append(root)
    explored = set()
    while True:
        if frontier.count == 0:
            return 0
        node = frontier.popleft()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            if child.state not in explored:
                if child.depth < level:
                    print(child.state + " > ")
                    if problem.goal_test(child.state):
                        return child
                    frontier.append(child)
                else:
                    return "cutoff"

def uniform_cost_search(problem):
    root = Node(problem.initial)
    frontier = PriorityQueue()
    frontier.append(root)
    explored = set()

    while True:
        if len(frontier) == 0:
            return "fail"
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            if child.state not in explored:
                print(child.state + " > ")
                frontier.append(child)
            elif child in frontier:
                item = frontier.__getitem__(child)
                if child.path_cost < item.path_cost:
                    pass

def print_info_about_search(node):
    print("The search algorithm reached " + node.state + " with a cost of " + str(node.path_cost) + ".")
    path = node.path()
    directions = ""
    for n in path:
        directions = directions + " > " + n.state
    print("The path is the following:" + directions)