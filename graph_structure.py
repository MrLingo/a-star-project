import math


class Graph:
    def __init__(self):
        self.node_list = []

    def add_node(self, node):
        self.node_list.append(node)

    def get_node(self, node_name):
        for n in self.node_list:
            if n.name == node_name:
                return n

    def create_link(self, start_node_name, end_node_name, cost, is_bidirectional, type):
        start_node = self.get_node(start_node_name)
        end_node = self.get_node(end_node_name)

        start_node.add_link(Link(end_node, cost, type))
        start_node.add_child_node(end_node)

        if is_bidirectional:
            end_node.add_link(Link(start_node, cost, type))
            end_node.add_child_node(start_node)


class Node:
    def __init__(self, name, distance_to_goal):
        self.distance_from_start = math.inf
        self.distance_to_goal = distance_to_goal  # Heuristic value - h(n).
        self.final_distance = 0  # f(n)
        self.is_colored = False  # Is visited.
        self.__child_nodes = []
        self.__links = []
        self.parent = None
        self.name = name

    def add_link(self, link):
        self.__links.append(link)

    @property
    def get_child_nodes(self):
        return self.__child_nodes

    @property
    def get_links(self):
        return self.__links

    def add_child_node(self, node):
        self.__child_nodes.append(node)

    # Comparators:
    def __le__(self, other):
        return self.final_distance <= other.final_distance

    def __lt__(self, other):
        return self.final_distance < other.final_distance


class Link:
    def __init__(self, to_node, cost, type):
        self.to_node = to_node
        self.cost = cost
        self.is_colored = False
        self.type = type

    # Types of links:
    # Static properties.
    transition = 'transition'
    standard = 'standard'
    roundabout = 'roundabout'
