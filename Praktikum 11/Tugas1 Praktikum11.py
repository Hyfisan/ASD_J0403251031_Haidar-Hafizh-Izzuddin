#===================================================================================

#Nama: Haidar Hafizh Izzuddin
#NIM: J0403251031
#Kelas: A2
#===================================================================================


def createGraph(V, edges): #Fungsi untuk membuat graph dengan representasi adjacency matrix
    mat = [[0 for _  in range(V)] for _ in range(V)]
    
    #Add eaach edges to the adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
        
        #Since the graph is undirected
        mat[v][u] = 1
    return mat

#Implementasi kode utama
if __name__ == "__main__":
    V = 4
    
    #List of edges (u, v)
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]] #List of edges yang akan dimasukkan ke dalam graph
    
    #Build the graph using edges
    mat = createGraph(V, edges)
    
    #Menampilkan representasi adjacency matrix
    print(f"""Nama: Haidar Hafizh Izzuddin
NIM: J0403251031
Kelas: A2""")
    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end = " ")
        print()