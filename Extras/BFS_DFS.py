from collections import defaultdict
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, fromNode, toNode):
        self.graph[fromNode].append(toNode)

    def BFS(self, startNode):
        visited = [0] * len(self.graph)
        Q = []
        Q.append(startNode)
        visited[startNode] = 1
        output = []
        output.append(startNode)
        while len(Q) > 0:
            node = Q.pop(0)
            edges = self.graph[node]
            for x in edges:
                if visited[x] == 0:
                    visited[x] = 1
                    output.append(x)
                    Q.append(x)
        print "BFS output: \n", output

    def DFS(self, startNode):
        visited = [0] * len(self.graph)

        stack = []
        stack.append(startNode)
        visited[startNode] = 1
        output = []
        output.append(startNode)
        while stack:
            node = stack[-1]
            edges = self.graph[node]
            for e in edges:
                if e in stack:
                    print "Cycle detected from ", node, "to ", e
            for x in edges:
                if visited[x] == 0:
                    visited[x] = 1
                    stack.append(x)
                    output.append(x)
                    break
                else:
                    continue
                stack.pop(-1)
            else:
                stack.pop(-1)

        print "DSF output \n", output

def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    #g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(1, 3)
    g.addEdge(3, 3)

    #g.addEdge(3, 4)
    #g.addEdge(4, 2)

    #g.BFS(0)
    g.DFS(0)

if __name__ == '__main__':
    main()