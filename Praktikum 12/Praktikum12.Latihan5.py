# Nama  : Haidar Hafizh Izzuddin
# NIM   : J0403251031
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Representasi graph berbobot menggunakan dictionary bersarang.
# Bobot menunjukkan jarak/biaya perjalanan antarkota.
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke semua node lain menggunakan algoritma Dijkstra.
    """

    # Inisialisasi jarak semua node sebagai tak hingga.
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke node awal adalah 0.
    distances[start] = 0

    # Priority queue digunakan agar node dengan jarak terkecil diproses lebih dulu.
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak yang diproses lebih besar dari jarak terbaik,
        # maka proses untuk node tersebut dilewati.
        if current_distance > distances[current_node]:
            continue

        # Periksa setiap tetangga dari node saat ini.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, update jarak dan masukkan ke queue.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Penentuan node awal dalam program.
start_node = 'Bogor'

hasil = dijkstra(graph, start_node)

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(start_node, "->", kota, "=", jarak)

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor.
# 2. Node yang memiliki jarak paling kecil dari node awal selain Bogor adalah Depok,
#    dengan jarak 2.
# 3. Node yang memiliki jarak paling besar dari node awal adalah Bandung,
#    dengan jarak 8.
# 4. Pada kasus ini, Dijkstra bekerja dengan memulai jarak Bogor = 0 dan kota lain
#    = tak hingga. Setelah itu, algoritma memilih node dengan jarak sementara
#    paling kecil. Dari Bogor, jarak ke Jakarta adalah 5 dan ke Depok adalah 2.
#    Karena Depok lebih kecil, Depok diproses lebih dulu. Dari Depok, jarak ke
#    Jakarta menjadi 2 + 2 = 4, lebih kecil dari 5, sehingga jarak Jakarta
#    diperbarui menjadi 4. Depok juga memberi jarak ke Bandung sebesar 2 + 6 = 8.
#    Setelah itu Jakarta diproses, tetapi jalur Jakarta -> Bandung menghasilkan
#    4 + 7 = 11, lebih besar dari 8, sehingga jarak Bandung tetap 8. Hasil akhir:
#    Bogor = 0, Depok = 2, Jakarta = 4, dan Bandung = 8.
