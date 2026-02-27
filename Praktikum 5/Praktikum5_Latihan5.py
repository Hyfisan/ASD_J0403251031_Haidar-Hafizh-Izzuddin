# ==========================================================
# Nama: Haidar Hafizh Izzuddin
# NIM: J0403251031
# Kelas: TPL A2
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
 if len(hasil) == panjang: # Jika panjang PIN sudah sesuai, maka cetak PIN
    print("PIN:", hasil)
    return

 for angka in ["0", "1", "2"]: # Loop setiap kemungkinan angka untuk PIN
    buat_pin(panjang, hasil + angka)
    
buat_pin(3)
