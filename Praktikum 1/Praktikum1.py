#==================================================================================================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca Seluruh Isi File
#==================================================================================================================================================


print ("---Membuka File Dalam Satu String---")
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    isi_file =  file.read()
print(isi_file)

print("---Hasil Read---")
print("Tipe Data :", type(isi_file))


#Membuka File per baris
print ("---Membuka File per baris---")
jumlah_baris = 0
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("Baris Ke-", jumlah_baris)
        print("Isinya :", baris)
        

#Parsing  baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data
jumlah_baris = 0
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai, = baris.split(",") #Pecah menjadi data satuan dan simpan ke variabel
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai)
        
        
        
        
#==================================================================================================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca Data dan Menyimpannya Ke Struktur Data List
#==================================================================================================================================================

data_list = []#inisialisasi list untuk menampung data

with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai, = baris.split(",") #Pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim, nama, int(nilai)])#mMenyimpan data ke list
print("Menampilkan List")
print(data_list)
print("Contoh Recprd Ke 1", data_list[0])
print("Contoh Recprd Ke 2", data_list[1])
print("Jumlah Record", len(data_list))


#==================================================================================================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca Data dan Menyimpannya Ke Struktur Data Dictionary
#==================================================================================================================================================

data_dict = {}

with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai, = baris.split(",") #Pecah menjadi data satuan dan simpan ke variabel
        #simpan data dalam dictionary
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }
        
print("---Menampilkan Data Dictionary---")
print(data_dict)