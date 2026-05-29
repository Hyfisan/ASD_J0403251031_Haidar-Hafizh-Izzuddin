# Nama : Haidar Hafizh Izzuddin
# NIM : J0403251031
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 3 - Implementasi Algoritma Prim
# ==========================================================
# Prim membangun MST secara bertahap dari satu node awal.

import heapq

# Representasi weighted graph menggunakan dictionary
# Format: node: {tetangga: bobot}
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


def prim(graph, start):
    # Menyimpan node yang sudah masuk ke MST
    visited = set([start])

    # Priority queue untuk menyimpan edge berdasarkan bobot terkecil
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Selama masih ada edge yang dapat diproses
    while edges:
        weight, u, v = heapq.heappop(edges)

        # Pilih edge jika node tujuan belum dikunjungi
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Masukkan edge dari node baru ke priority queue
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah A.
# 2. Edge yang dipilih pertama kali adalah A-C dengan bobot 2.
# 3. Prim menentukan edge berikutnya dengan memilih edge berbobot paling kecil yang
#    menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi.
# 4. Total bobot MST yang dihasilkan adalah 6.
# 5. Perbedaan Prim dan Kruskal adalah Prim membangun tree dari node awal, sedangkan
#    Kruskal memilih edge terkecil secara global dari seluruh graph.