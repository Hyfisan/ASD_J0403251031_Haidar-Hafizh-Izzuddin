#------------------------------------------------------------------ 
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 1: Membuat Fungsi Load dari Data Fle
#------------------------------------------------------------------ 

#Variable menyimpan data
nama_file = "data_mahasiswa.txt"
def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
       for baris in file:
        baris = baris.strip() #ambil data per baris dan hilangkan new line
        nim, nama, nilai = baris.split(",") #memisahkan data berdasarkan koma
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
            } #simpan data ke dictionary
    return data_dict

#buka_data = baca_data(nama_file) #Memanggil fungsi load data dan menyimpan ke variable
#print ("Jumlah Data Terbaca", len(buka_data)) #Melihat berapa data yang di load
    

    
#------------------------------------------------------------------ 
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 1: Membuat Fungsi Menampilkan Data
#------------------------------------------------------------------ 

def tampilkan_data(data_dict):
    #membuat header table
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    print("-" * 35) #membuat garis pemisah
    
    #Menampilkan isi datanya
    for nim in sorted(data_dict.keys()): #mengurutkan berdasarkan NIM
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {nilai : >5}")

#tampilkan_data(buka_data) #memanggil fungsi tampilkan data



#------------------------------------------------------------------ 
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 3: Membuat Fungsi Mencari Data
#------------------------------------------------------------------ 

#Membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan NIM
    nim_cari = input("Masukkan NIM Mahasiswa yang ingin dicari: ").strip()
    
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("\n=== Data Mahasiswa Ditemukan ===")
        print(f"NIM  : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai: {nilai}")
        
    else:
        print("\nData Mahasiswa tidak ditemukan. Pastikan NIM yang dimasukkan benar.")

#Memanggil fungsi pencarian data
#cari_data(buka_data) 

#------------------------------------------------------------------ 
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 4: Membuat Fungsi Update Data
#------------------------------------------------------------------ 

#Membuat fungsi update data
def ubah_data(data_dict):
    
    #Awali dengan mencari nim / data mahasiswa yang ingin diubah
    nim = input("Masukkan NIM Mahasiswa yang ingin diubah datanya: ").strip()
    
    if nim not in data_dict:
        print("\nData Mahasiswa tidak ditemukan. Pastikan NIM yang dimasukkan benar.")
        return
    
    try:
        nilai_baru = int(input(f"Masukkan Nilai Baru 0 - 100 : ").strip())
    except ValueError:
        print("Nilai harus berupa angka antara 0 hingga 100.")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 hingga 100.")
        return
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = (nilai_baru)
    
    print(f"Update berhasil. Nilai Mahasiswa dengan NIM {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.")
    
#memanggil fungsi update data
#ubah_data(buka_data)


#------------------------------------------------------------------ 
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 5: Membuat Fungsi Menimpan Data Pada File
#------------------------------------------------------------------ 

#Membuat fungsi simpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n") 
            
#memanggil fungsi simpan data
#simpan_data(nama_file, buka_data)
#print("\nData berhasil disimpan kembali ke file.", nama_file)


#------------------------------------------------------------------ 
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 6: Membuat Menu Interaktif
#------------------------------------------------------------------ 

def main():
    nama_file = "data_mahasiswa.txt"
    data_dict = baca_data(nama_file)
    
    while True:
        print("\n=== Menu Interaktif ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Simpan Data ke File")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            tampilkan_data(data_dict) #Memanggil fs.2 menampilkan data
        elif pilihan == "2":
            cari_data(data_dict) #Memanggil fs.3 mencari data
        elif pilihan == "3":
            ubah_data(data_dict) #Memanggil fs.4 mengubah data
        elif pilihan == "4":
            simpan_data(nama_file, data_dict) #Memanggil fs.5 menyimpan data
            print("Data berhasil disimpan.")
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
main()