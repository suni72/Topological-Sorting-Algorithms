from collections import defaultdict


class Graph(object):
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function for Toppological sorting
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited
        visited[v] = True

        # Recur all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)

    # The function to execute Topological sort
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological Sort starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of the stack
        print(stack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")
g.topologicalSort()