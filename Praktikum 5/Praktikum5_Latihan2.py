# ==========================================================
# Nama: Haidar Hafizh Izzuddin
# NIM: J0403251031
# Kelas: TPL A2
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
 if n == 0: # Jika n == 0, maka berhenti dan cetak "Selesai"
    print("Selesai")
    return

 print("Masuk:", n)  # Fase Masuk (stacking)
 
 countdown(n - 1)  # Pemanggilan rekursif
 
 print("Keluar:", n) # Fase Keluar (unwinding)
 
countdown(3)