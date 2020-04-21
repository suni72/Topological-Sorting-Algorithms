from collections import defaultdict


class Graph(object):
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Topological Sorting
    def topologicalSort(self):

        # Create a vector to store indegrees o all vertices
        # Initialize all degrees as 0
        in_degree = [0] * self.V

        # Traverse the adjacent lists to fill indegrees of vertices
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create a queue and enqueue all vertices with indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        count = 0

        # Create a vector to store results
        top_order = []

        # One by one dequeue vertices from queue and enqueue adjacents if indegree of adjacent becomes 0
        while queue:
            # Extract front of queue and add it to topological order
            u = queue.pop(0)
            top_order.append(u)

            # Iterate through all the neighbouring nodes
            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

            count += 1

        # Check for cycles
        if count != self.V:
            print("There is a cycle in the graph.")
        else:
            print(top_order)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")
g.topologicalSort()
