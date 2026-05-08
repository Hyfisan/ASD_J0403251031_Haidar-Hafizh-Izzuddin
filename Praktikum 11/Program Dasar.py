def createGraph(V, edges):
    mat = [[0 for _  in range(V)] for _ in range(V)]
    
    #Add eaach edges to the adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
        
        #Since the graph is undirected
        mat[v][u] = 1
    return mat

if __name__ == "__main__":
    V = 3
    
    #List of edges (u, v)
    edges = [[0, 1], [0, 2], [1, 2]]
    
    #Build the graph using edges
    mat = createGraph(V, edges)
    
    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end = " ")
        print()