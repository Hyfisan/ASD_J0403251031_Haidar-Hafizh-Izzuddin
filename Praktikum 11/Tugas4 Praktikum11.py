#===================================================================================
#Nama: Haidar Hafizh Izzuddin
#NIM: J0403251031
#Kelas: A2
#===================================================================================


# ==============================================================
# DESKRIPSI STUDI KASUS
# ==============================================================
# Platform media sosial mini dengan 6 akun pengguna.
# Hubungan antar pengguna bersifat "follow" (satu arah / directed).
# Seseorang bisa follow orang lain tanpa harus di-follow balik.
#
# Node (Vertex) — 6 pengguna:
#   0 = Hafizh
#   1 = Hanif
#   2 = Daud
#   3 = Ilham
#   4 = Reihan
#   5 = Azmi
#   6 = Adit
# ==============================================================

# --- Data utama ---
nodes = ["Hafizh", "Hanif", "Daud", "Ilham", "Reihan", "Azmi", "Adit"]
V = len(nodes)  # jumlah vertex = 6

# Edge dalam format (u, v) = u follow v
edges = [
    (0, 1),  # Hafizh  -> Hanif
    (0, 2),  # Hafizh  -> Daud
    (0, 3),  # Hafizh  -> Ilham
    (0, 4),  # Hafizh  -> Reihan
    (0, 5),  # Hafizh  -> Azmi
    (1, 2),  # Hanif  -> Daud
    (1, 6),  # Hanif -> Adit
    (2, 1),  # Daud -> Hanif
    (2, 3),  # Daud -> Ilham
    (3, 4),  # Ilham -> Reihan
    (4, 3),  # Reihan -> Ilham
    (5, 4),  # Azmi -> Reihan
    (6, 0),  # Adit -> Hafizh
]

# ==============================================================
# FUNGSI PEMBANTU
# ==============================================================

def buat_adjacency_list(V, edges):
    adj = [[] for _ in range(V)]
    for (u, v) in edges:
        adj[u].append(v)   # directed: hanya satu arah
    return adj


def buat_adjacency_matrix(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]
    for (u, v) in edges:
        mat[u][v] = 1      # directed: hanya satu arah
    return mat


def tampilkan_adjacency_list(adj, nodes):
    print("=" * 50)
    print("  ADJACENCY LIST - Media Sosial (Follow)")
    print("=" * 50)
    for i in range(len(adj)):
        tetangga = [nodes[j] for j in adj[i]]
        if tetangga:
            print(f"  {nodes[i]:<8} -->  {', '.join(tetangga)}")
        else:
            print(f"  {nodes[i]:<8} -->  (tidak follow siapapun)")
    print()


def tampilkan_adjacency_matrix(mat, nodes):
    print("=" * 50)
    print("  ADJACENCY MATRIX - Media Sosial (Follow)")
    print("=" * 50)
    # Header kolom
    header = "         " + "  ".join(f"{n[:4]:>5}" for n in nodes)
    print(header)
    print("         " + "-" * (len(nodes) * 7))
    # Isi baris
    for i in range(len(mat)):
        baris = "  ".join(f"{mat[i][j]:>5}" for j in range(len(mat[i])))
        print(f"  {nodes[i]:<7} | {baris}")
    print()


def tampilkan_penjelasan_matrix(mat, nodes):
    print("=" * 50)
    print("  PENJELASAN SETIAP BARIS ADJACENCY MATRIX")
    print("=" * 50)
    for i in range(len(mat)):
        following = [nodes[j] for j in range(len(mat[i])) if mat[i][j] == 1]
        if following:
            print(f"  Baris {nodes[i]:<8}: follow -> {', '.join(following)}")
        else:
            print(f"  Baris {nodes[i]:<8}: tidak follow siapapun")
    print()


# ==============================================================
# MAIN PROGRAM
# ==============================================================

if __name__ == "__main__":
    print(f"""Nama: Haidar Hafizh Izzuddin
NIM: J0403251031
Kelas: A2""")
    
    # Bangun struktur data
    adj = buat_adjacency_list(V, edges)
    mat = buat_adjacency_matrix(V, edges)

    # Tampilkan output
    tampilkan_adjacency_list(adj, nodes)
    tampilkan_adjacency_matrix(mat, nodes)
    tampilkan_penjelasan_matrix(mat, nodes)

