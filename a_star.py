import graph_structure as gs


class AStar:
    def __init__(self):
        self.queue = []
        self.standard_links = 0
        self.roundabout_links = 0
        self.transition_links = 0

    def __calculate_distance(self, parent_node, start_node, graph):
        for link in parent_node.get_links:
            if link.to_node == start_node:
                continue
            child_node = graph.get_node(link.to_node.name)

            # Compare the distance to goal of the parent node to the child one. If it's less assign it to the child.
            if child_node.parent is None or child_node.distance_from_start > parent_node.distance_from_start + link.cost:
                child_node.parent = parent_node
                child_node.distance_from_start = parent_node.distance_from_start + link.cost

        # f(n) = g(n) + h(n):
        if parent_node.final_distance < child_node.final_distance:
            child_node.final_distance = parent_node.final_distance

    def __print_path(self, end_node, start_node):
        print('\nThere is a path!\n')
        temp_list = []
        temp_node = end_node
        print(start_node.name, end=' | ')

        while temp_node.parent is not None:
            self.get_link_type(temp_node.parent, temp_node)
            temp_list.append(temp_node.name)
            temp_node = temp_node.parent

        for n in reversed(temp_list):
            print(n, end=' | ')
        temp_list.append(start_node.name)
        return temp_list

    def get_link_type(self, parent_node, child_node):
        links = child_node.get_links
        for l in links:
            if l.to_node is parent_node:
                if l.type is gs.Link.standard:
                    self.standard_links += 1
                    break
                elif l.type is gs.Link.transition:
                    self.transition_links += 1
                    break
                elif l.type is gs.Link.roundabout:
                    self.roundabout_links += 1
                    break
                else:
                    print('Invalid link type!')
                    break

    def search(self, graph, start_node_name, end_node_name):
        if not isinstance(graph, gs.Graph) or not isinstance(start_node_name, str) \
                or not isinstance(end_node_name, str):
            raise ValueError('Cannot proceed with passed None types!')

        # Find the nodes and start the search:
        start_node = graph.get_node(start_node_name)
        end_node = graph.get_node(end_node_name)

        start_node.distance_from_start = 0

        if start_node in graph.node_list and end_node in graph.node_list:
            if start_node != end_node:
                self.queue.append(start_node)

                while len(self.queue) > 0:
                    temp = self.queue[0]
                    self.__calculate_distance(temp, start_node, graph)
                    print('Temp node is : ' + temp.name)

                    if temp == end_node:
                        self.__print_path(end_node, start_node)
                        return True

                    temp.is_colored = True

                    # Remove the last element.
                    self.queue.pop(0)

                    for node in temp.get_child_nodes:
                        if node not in self.queue and node.is_colored is False:
                            self.queue.append(node)

                    # Sort by final distance.
                    self.queue.sort()

                # If there is no path return False.
                print('There is no path!')
                return False
            else:
                print('The start node is also the end node!')
                return False
        else:
            print('One (Or both) of the nodes is/are not in the given graph!')
            return False
