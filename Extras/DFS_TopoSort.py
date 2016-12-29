from collections import defaultdict

current_label = 2

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, fromNode, toNode):
        self.graph[fromNode].append(toNode)


    def DFS_loop(self):
        #current_label = self.vertices
        global current_label
        visited = [0] * current_label
        topo_sort = [0] * current_label
        for edge in xrange(0,current_label):
            if visited[edge] == 0:
                visited[edge] = 1
                self.DFS(edge, visited, topo_sort)#, current_label)

        for i in xrange(1,7):
            print topo_sort.index(i),

    def DFS(self, edge, visited, topo_sort): #, current_label):
        global current_label
        for every_edge in self.graph[edge]:
            if visited[every_edge] == 0:
                visited[every_edge] = 1
                self.DFS(every_edge, visited, topo_sort)
        topo_sort[edge] = current_label
        current_label -= 1

def main():
    g = Graph(6)
    global current_label
    print current_label
    current_label = 6

    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(5, 1)
    g.addEdge(5, 2)
    g.DFS_loop()
    #g.addEdge(0, 1)
    #g.addEdge(0, 2)
    #g.addEdge(2, 3)
    #g.addEdge(1, 3)
'''
    g.addEdge(4, 1)
    g.addEdge(3, 1)
    g.addEdge(2, 3)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)'''
    #g.DFS_loop()

    #Note: can be used to assign directions to edges so that the directed graph remains acyclic.

if __name__ == '__main__':
    main()