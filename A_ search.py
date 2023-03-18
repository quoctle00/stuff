class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1,
            'G': 1,
            'H': 1,
            'I': 1,
            'J': 1,
            'K': 1
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            # start writing from here
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;
                    
        print('Path does not exist!')
        return None


if __name__ == '__main__':

	adjacency_list1 = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

adjacency_list2 = {
    'A': [('B', 1)],
    'B': [('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 5), ('K', 11)],
    'E': [('G', 7), ('F', 8)],
    'F': [('I', 4), ('J', 9)],
    'G': [('H', 11), ('I', 8)],
    'H': [('I', 4)],
    'J': [('I', 13)],
    'K': [('J', 3)]
}

graph1 = Graph(adjacency_list1)
graph1.a_star_algorithm('A', 'D')

graph1 = Graph(adjacency_list2)
graph1.a_star_algorithm('A', 'I')