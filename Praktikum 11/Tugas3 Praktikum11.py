#===================================================================================
#Nama: Haidar Hafizh Izzuddin
#NIM: J0403251031
#Kelas: A2
#===================================================================================

matrix = [
    [0,1,1,0],
    [1,0,1,0],
    [1,1,0,1],
    [0,0,1,0]
]

def convertToAdjList(matrix):
    adjList = {}
    for i in range(len(matrix)):
        adjList[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adjList[i].append(j)
    return adjList

if __name__ == "__main__":
    print(f"""Nama: Haidar Hafizh Izzuddin
NIM: J0403251031
Kelas: A2""")
    adjList = convertToAdjList(matrix)
    for node in sorted(adjList):
        print(f"{node}: {adjList[node]}")