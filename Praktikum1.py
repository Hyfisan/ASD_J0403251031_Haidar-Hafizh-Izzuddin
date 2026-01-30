#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca Seluruh Isi File



print ("---Membuka File Dalam Satu String---")
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    isi_file =  file.read()
print(isi_file)

print("Tipe Data :", type(isi_file))


print ("---Membuka File per baris---")
jumlah_baris = 0 #inisialisasi
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris
        print("Baris Ke-", jumlah_baris)
        print("Isinya :", baris)
        
print("Aku Bisa YEY")
