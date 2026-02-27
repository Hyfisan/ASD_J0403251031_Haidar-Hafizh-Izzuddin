# ==========================================================
# Nama: Haidar Hafizh Izzuddin
# NIM: J0403251031
# Kelas: TPL A2
# Latihan 1: Rekursi Pangkat
# ==========================================================


def pangkat(a, n): # Fungsi rekursif untuk menghitung pangkat a^n
 # Base case
 if n == 0:  # Jika n == 0, maka hasil pangkat adalah 1
    return 1

 # Recursive case
 return a * pangkat(a, n - 1) # Fungsi memanggil dirinya sendiri dengan nilai n dikurangi 1

print(pangkat(2, 4)) # Output: 16
