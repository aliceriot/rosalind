
class edge_list_graph:
    def __init__(self,graph_string):
        graph = [[int(i) for i in k.split(' ')] for k in graph_string.split('\n') if k != '']
        self.nodes = graph[0][0]
        self.edgenum = graph[0][1]
        self.vertices = {key: 0 for key in range(1,nodes + 1)}
        for i in graph[1:]:
            self.vertices[i[0]] += 1
            self.vertices[i[1]] += 1

    def print_vertices(self):
        print self.vertices.values()

 

with open ("/home/benpote/Downloads/rosalind_deg (2).txt", "r") as myfile:
    data = myfile.read()

mygraph = edge_list_graph(data)
mygraph.print_vertices()


#formatting for how rosalind wants the answer

" ".join([str(i) for i in mygraph.vertices.values()])


#it works! noice!
