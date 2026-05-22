# Nama : Haidar Hafizh Izzuddin
# NIM : J0403251031
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}
# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")
    
# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 9, karena A -> B = 4 dan B -> D = 5.
# 2. Total bobot jalur A -> C -> D adalah 3, karena A -> C = 2 dan C -> D = 1.
# 3. Jalur yang dipilih sebagai jalur terpendek adalah A -> C -> D.
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit,
#    karena shortest path berfokus pada total bobot terkecil. Walaupun dua jalur
#    memiliki jumlah edge yang sama atau bahkan ada jalur yang memiliki edge lebih
#    banyak, jalur dengan total bobot paling kecil tetap menjadi jalur terbaik.
