class Graph:
    def __init__(self,num_of_nodes,directed=True):
        self.num_of_nodes=num_of_nodes
        self.nodes=range(self.num_of_nodes)
        self.directed=directed
        self.adj_list={node : set() for node in self.nodes}
        'self.adj_list=dict()'

    def add_edge(self,vertex1,vertex2,weight=1):
        '''if vertex1 not in self.adj_list.keys():
            self.adj_list[vertex1]={(vertex2, weight)}
        else:
            self.adj_list[vertex1].add((vertex2, weight))'''
        self.adj_list[vertex1].add((vertex2, weight))
        if not self.directed:
            self.adj_list[vertex2].add((vertex1, weight))

    def print_adj_list(self):
        for vertex1,vertex2 in self.adj_list.items():
            print("Node",vertex1,":",vertex2)

graph=Graph(5)
graph.add_edge(0,1,5)
graph.add_edge(0,0,25)
graph.add_edge(0,2,3)
graph.add_edge(1,4,15)
graph.add_edge(1,3,1)
graph.add_edge(4,2,7)
graph.add_edge(4,3,11)

print("Adjacency List:")
graph.print_adj_list()