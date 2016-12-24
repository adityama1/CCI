'''The king decided to start introducing the changes with something more or less simple: change all the roads in the kingdom from two-directional to one-directional.
He personally prepared the roadRegister of the new roads, and now he needs to make sure that the road system is convenient and there will be no traffic jams, i.e.
each city has the same number of incoming and outgoing roads.
As the Hand of the King, you're the one who should check it.'''


def newRoadSystem(roadRegister):
    num_of_nodes = len(roadRegister[0])
    visited = [0] * num_of_nodes
    edges_count_out = [0] * num_of_nodes
    edges_count_in = [0] * num_of_nodes
    Q = []
    for i in xrange(0, num_of_nodes):
        if visited[i] == 0:
            visited[i] = 1
            Q.append(i)
            while len(Q):
                node = Q.pop(0)
                for x in xrange(0, num_of_nodes):
                    if roadRegister[node][x] is True:
                        edges_count_out[node] += 1
                        if visited[x] == 0:
                            visited[x] = 1
                            edges_count_in[x] += 1
                            Q.append(x)
                        else:
                            edges_count_in[x] += 1

    print edges_count_out
    print edges_count_in
    a = 0
    for x,y in zip(edges_count_out, edges_count_in):
        if x == y:
            a += 1
    if a == num_of_nodes:
        return True
    else:
        return False


def main():
    false = False
    true = True

    road = [[false,true,true,false,true],
             [true,false,false,true,false],
             [false,true,false,true,false],
             [true,true,true,false,true],
             [true,true,false,false,false]]
    #print zip(*road)

    roads = [[5, 8],
             [6, 0],
             [0, 5],
             [4, 1],
             [0, 1],
             [7, 0],
             [6, 8],
             [7, 3],
             [2, 6],
             [0, 2],
             [0, 3],
             [8, 7],
             [5, 4],
             [8, 4],
             [8, 2],
             [7, 1],
             [4, 6],
             [5, 6],
             [4, 2],
             [4, 7],
             [2, 7],
             [3, 6],
             [8, 0],
             [1, 6],
             [3, 2],
             [3, 4],
             [4, 0],
             [6, 7],
             [5, 7]]
    roads = [[0, 1], [1, 2], [2, 0]]
    cities = 4
    output = []

    #Question 2.
    for i in xrange(0,cities):
        for j in xrange(i+1, cities):
            if [i,j] not in roads and [j,i] not in roads:# and i != j:
                #if [i,j] and [j,i] not in output:
                    output.append([i,j])

    print output
    #print zip(*roads)
'''
    Alternate Solution:
    def newRoadSystem(roadRegister):
#    print zip(*roadRegister)
    for m in range(len(roadRegister)):
        if sum(roadRegister[m]) != sum (zip(*roadRegister)[m]): return False
    return True

    F***ing awesome!
    '''

if __name__ == '__main__':
    main()



