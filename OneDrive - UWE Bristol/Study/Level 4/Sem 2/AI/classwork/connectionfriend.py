import sys
import csv

class Node:
    def __init__(self, state, parent, action, h_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.h_cost = h_cost
    
class StackFrontier:
    def __init__(self):
        self.frontier = []
        
    def add(self, node):
        self.frontier.append(node)
        
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
class PriorityQueueFrontier(QueueFrontier):
    def add(self, node):
        self.frontier.append(node)
        self.frontier.sort(key=lambda x: x.h_cost)

def load_connections(file_path):
    connections = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for user1, user2 in reader:
            connections.setdefault(user1, []).append(user2)
            connections.setdefault(user2, []).append(user1)
    return connections

def find_connection(connections, start_user, target_user):
    if start_user not in connections or target_user not in connections:
        return None  
    
    frontier = PriorityQueueFrontier()
    node = Node(state=start_user, parent=None, action=None, h_cost=0)
    frontier.add(node)
    explored = set()
    
    while True:
        if frontier.empty():
            return None 
        
        node = frontier.remove()
        if node.state == target_user:
            path = []
            while node is not None:
                path.append(node.state)
                node = node.parent
            path.reverse()
            return path
        
        explored.add(node.state)
        for friend in connections[node.state]:
            if friend not in explored and not frontier.contains_state(friend):
                child = Node(state=friend, parent=node, action=None, h_cost=0)
                frontier.add(child)

if __name__ == "__main__":
    file_path = 'data.csv'
    connections = load_connections(file_path)
    start = 'user_31'  
    target = 'user_11'  

    path = find_connection(connections, start, target)
    if path:
        print("User's friends are:\n", " -> ".join(path))
    else:
        print("No connection found between", start, "and", target)
