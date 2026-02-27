# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
 if len(hasil) == n: # Jika panjang hasil sudah sama dengan n, maka cetak kombinasi
    print(hasil)
    return

# Choose + Explore huruf A
 kombinasi(n, hasil + "A")
 
# Choose + Explore huruf A
 kombinasi(n, hasil + "B")
 
kombinasi(2)