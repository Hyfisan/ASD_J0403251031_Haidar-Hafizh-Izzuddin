# ==========================================================
# Nama: Haidar Hafizh Izzuddin
# NIM: J0403251031
# Kelas: TPL A2
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):
 # Base case
 # Jika index sudah berada di elemen terakhir, maka elemen tersebut adalah maksimum sementara
 if index == len(data) - 1:
    return data[index]

 # Recursive case
 maks_sisa = cari_maks(data, index + 1) # Cari maksimum dari sisa elemen setelah index sekarang
 
 if data[index] > maks_sisa: # Bandingkan elemen sekarang dengan maksimum sisa
    return data[index]
 else:
    return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))