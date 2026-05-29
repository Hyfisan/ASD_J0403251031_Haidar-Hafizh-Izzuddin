# Nama : Haidar Hafizh Izzuddin
# NIM : J0403251031
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 2 - Implementasi Sederhana Algoritma Kruskal
# ==========================================================
# Kruskal memilih edge dengan bobot terkecil terlebih dahulu.

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge yang dipilih pertama kali adalah C-D dengan bobot 1.
# 2. Edge dengan bobot paling kecil dipilih lebih dahulu karena tujuan Kruskal adalah
#    membentuk MST dengan total bobot minimum.
# 3. Total bobot MST yang dihasilkan adalah 6, yaitu 1 + 2 + 3.
# 4. Edge A-B dan A-D tidak dipilih karena node-node tersebut sudah terhubung melalui
#    edge yang lebih kecil. Jika tetap dipilih, edge tersebut dapat membentuk cycle
#    dan menambah total bobot.