#!/usr/bin/python

#continuing with our theme of OOP practice:

class double_degree_array:
    def __init__(self,graph_string):
        edges = [[int(i) for i in k.split(' ')] for k in graph_string.split('\n') if k != '']
        self.nodes = edges[0][0]
        self.edgenum = edges[0][1]
        self.vertex_degrees = {key: 0 for key in range(1,self.nodes + 1)}
        self.vertex_edges = {key: [] for key in range(1,self.nodes + 1)}
        for i in edges[1:]:
            self.vertex_degrees[i[0]] += 1
            self.vertex_degrees[i[1]] += 1
            self.vertex_edges[i[0]].append(i[1])
            self.vertex_edges[i[1]].append(i[0])

    def neighbor_degree_sum(self):
        return [sum([self.vertex_degrees[i] for i in k])
                for k in self.vertex_edges.values()]



with open ("/home/benpote/Downloads/rosalind_ddeg.txt", "r") as myfile:
   data = myfile.read()

mygraph = double_degree_array(data)

#formatting for how rosalind wants the answer

x = " ".join([str(i) for i in mygraph.neighbor_degree_sum()])

