class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        self.neighbors = self.getAdjacnecyLists(edges)

    # Return a list of adjacency lists for edges 
    def getAdjacnecyLists(self, edges):
        neighbors = []
        for i in range(len(self.vertices)):
            neighbors.append([]) # Each element is another list
            
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            neighbors[u].append(Edge(u, v)) # Insert an edge (u, v)

        return neighbors
    
    # Return the number of vertices in the graph 
    def getSize(self):
        return len(self.vertices)

    # Return the vertices in the graph 
    def getVertices(self):
        return self.vertices

    # Return the vertex at the specified index
    def getVertex(self, index):
        return self.vertices[index]

    # Return the index for the specified vertex 
    def getIndex(self, v):
        return self.vertices.index(v)

    # Return the neighbors of vertex with the specified index 
    def getNeighbors(self, index):
        return self.neighbors[index]
    
    # Return the degree for a specified vertex 
    def getDegree(self, v):
        return len(self.neighbors[self.getIndex(v)])

    # Print the edges 
    def printEdges(self):
        for u in range(0, len(self.neighbors)):
            print(str(self.getVertex(u)) + " (" + str(u), end = "): ")
            for j in range(len(self.neighbors[u])):
                print("(" + str(u) + ", " + 
                      str(self.neighbors[u][j].v), end = ") ")
            print()

    # List of friends with names
    def printFriendList(self):
        for u in range(0, len(self.neighbors)):
            print("Friends of " + str(self.getVertex(u)), end = ": ")
            friendslist = []
            for j in range(len(self.neighbors[u])):
                friendslist.append(str(self.getVertex(self.neighbors[u][j].v)))
            friendslist = ','.join(friendslist)
            print(friendslist)
            
    # Clear graph 
    def clear(self):
        vertices = []
        neighbors = []
  
    # Add a vertex to the graph   
    def addVertex(self, vertex):
        if not (vertex in self.vertices):
            self.vertices.append(vertex)
            self.neighbors.append([]) # add a new empty adjacency list
        
    # Add an undirected edge to the graph   
    def addEdge(self, u, v):
        if u in self.vertices and v in self.vertices:
            indexU = self.getIndex(u)
            indexV = self.getIndex(v)
            # Add an edge (u, v) to the graph
            self.neighbors[indexU].append(Edge(indexU, indexV))

# The Edge class for defining an edge from u to v        
class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v


# Social Network
vertices = ["Peter", "Jane", "Mark", "Cindy", "Wendy"]

edges = [[0,1], [0,2], [1,0], [1,2], [1,3], [2,0], [2,1], [2,3], [2,4], [3,1], [3,2], [3,4], [4,2], [4,3]]

friend_graph = Graph(vertices, edges)


display = True
while display == True:
    new_user = str(input("Enter your name: "))
    friend_graph.addVertex(new_user)
    adding_friends = True
    while adding_friends == True:
        

        print("Select who you would like to add from this list, one at a time. Enter -1 to exit.")
        number = 0
        choices = []
        for name in vertices:
            choices.append(str(number) + ": " + str(name))
            number += 1

        for x in range(len(choices)):
            print(choices[x], end = "\n")

        select = int(input("Which would you like to add? "))
        if select == 0:
            friend_graph.addEdge(new_user, vertices[select])
            friend_graph.addEdge(vertices[select], new_user)
            print("You have befriended", vertices[select])
    
        if select == 1:
            friend_graph.addEdge(new_user, vertices[select])
            friend_graph.addEdge(vertices[select], new_user)
            print("You have befriended", vertices[select])

        if select == 2:
            friend_graph.addEdge(new_user, vertices[select])
            friend_graph.addEdge(vertices[select], new_user)
            print("You have befriended", vertices[select])

        if select == 3:
            friend_graph.addEdge(new_user, vertices[select])
            friend_graph.addEdge(vertices[select], new_user)
            print("You have befriended", vertices[select])

        if select == 4:
            friend_graph.addEdge(new_user, vertices[select])
            friend_graph.addEdge(vertices[select], new_user)
            print("You have befriended", vertices[select])

        if select == -1:
            adding_friends = False
    
    print("The friend list for all users: " + "\n")
    friend_graph.printEdges()

    friend_graph.printFriendList()
    display = False