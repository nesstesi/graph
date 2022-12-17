class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
            self.graph_dict = graph_dict

    def __iter__(self):
        self.iter_obj = iter(self.graph_dict)
        return self.iter_obj

    def __next__(self):
        return next(self.iter_obj)

    def __str__(self):
        result = 'nodes: '
        for key in self.graph_dict:
            result += str(key) + ' '
            result += 'edges: '
        return result

    def add_node(self, node):
        self.node = input('Please enter a name of vertex: \n')
        if node not in self.graph_dict:
            self.graph_dict[node] = []

    def add_edge(self, first_edge, second_edge):
        self.first_edge = input('Please enter a name of start edge: \n')
        self.second_edge = input('Please enter a name of finish edge: \n')
        if first_edge in self.graph_dict:
            self.graph_dict[first_edge].append(second_edge)
        else:
            self.graph_dict[first_edge] = [second_edge]

    def find_edge(self):
        edge_name = []
        for key in self.graph_dict:
            for value in self.graph_dict[key]:
                if {value, key} not in edge_name:
                    edge_name.append({key, value})
                    return True
                else:
                    return False
        return edge_name

if __name__ == '__main__' :

    graph_elements = {
        '1' : [2, 3],
        '2' : [1, 4],
        '3' : [1, 3],
        '4' : [2],
        '5' : [1, 4],
        '6' : []
    }
    graph = Graph(graph_elements)
    graph.add_node(7)
    graph.add_edge(5,4)
    print(graph)
