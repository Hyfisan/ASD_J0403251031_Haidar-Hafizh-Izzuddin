# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama :
# NIM :
# Kelas :
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"


# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
    - stok_dict (dictionary)
      key = kode_barang
      value = {"nama": nama_barang, "stok": stok_int}
    """
    stok_dict = {}

    # Membuka file dalam mode baca
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            # Membaca setiap baris di dalam file
            for baris in f:
                # Menghapus karakter newline di akhir baris
                baris = baris.strip()

                # Memisahkan data berdasarkan koma
                kode, nama, stok = baris.split(",")

                # Menyimpan data ke dictionary
                stok_dict[kode] = {
                    "nama": nama,
                    "stok": int(stok)  # Konversi stok ke integer
                }
    except FileNotFoundError:
        # Jika file belum ada, stok dianggap kosong
        pass

    return stok_dict


# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    # Membuka file dalam mode write
    with open(nama_file, "w", encoding="utf-8") as f:
        # Menulis setiap data barang ke file
        for kode in stok_dict:
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode},{nama},{stok}\n")


# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    # Mengecek apakah stok kosong
    if not stok_dict:
        print("Stok barang kosong.")
        return

    # Menampilkan header tabel
    print("Kode | Nama Barang | Stok")
    print("-" * 30)

    # Menampilkan seluruh data barang
    for kode in stok_dict:
        print(f"{kode} | {stok_dict[kode]['nama']} | {stok_dict[kode]['stok']}")


# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip()

    # Mengecek apakah kode ada di dictionary
    if kode in stok_dict:
        print("Barang ditemukan:")
        print("Nama :", stok_dict[kode]["nama"])
        print("Stok :", stok_dict[kode]["stok"])
    else:
        print("Barang tidak ditemukan.")


# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip()
    nama = input("Masukkan nama barang: ").strip()

    # Validasi kode agar tidak duplikat
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    # Input stok awal dan konversi ke integer
    stok_awal = int(input("Masukkan stok awal: "))

    # Menyimpan data barang baru ke dictionary
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print("Barang berhasil ditambahkan.")


# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    # Mengecek apakah kode ada di dictionary
    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()

    # Input jumlah perubahan stok
    jumlah = int(input("Masukkan jumlah: "))

    if pilihan == "1":
        # Menambah stok
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambah.")
    elif pilihan == "2":
        # Mengurangi stok
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Error: stok tidak boleh negatif.")
        else:
            stok_dict[kode]["stok"] -= jumlah
            print("Stok berhasil dikurangi.")
    else:
        print("Pilihan tidak valid.")


# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


# Menjalankan program utama
main()