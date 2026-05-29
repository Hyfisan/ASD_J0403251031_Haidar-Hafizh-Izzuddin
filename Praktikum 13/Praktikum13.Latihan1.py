# Nama : Haidar Hafizh Izzuddin
# NIM : J0403251031
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 1 - Memahami Konsep Spanning Tree
# ==========================================================
# Program ini menampilkan edge pada graph awal dan contoh
# spanning tree yang valid.

# Daftar edge pada graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
# Spanning tree memiliki seluruh node, tidak memiliki cycle,
# dan jumlah edge = jumlah node - 1.
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Perbedaan graph awal dan spanning tree adalah graph awal memiliki semua edge
#    yang tersedia sehingga dapat membentuk cycle, sedangkan spanning tree hanya
#    memilih sebagian edge yang menghubungkan semua node tanpa cycle.
# 2. Spanning tree tidak boleh memiliki cycle karena cycle menyebabkan edge berlebih
#    dan membuat koneksi menjadi tidak efisien.
# 3. Jumlah edge spanning tree selalu lebih sedikit karena spanning tree hanya
#    membutuhkan jumlah edge sebanyak jumlah node - 1 untuk menghubungkan semua node.