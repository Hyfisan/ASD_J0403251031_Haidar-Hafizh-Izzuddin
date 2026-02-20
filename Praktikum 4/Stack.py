#==========================================================================
#Nama: Haidar Hafizh Izzuddin
#NIM: J0403251031
#Kelas: TPL A2
#==========================================================================

#--------------------------------------------------------------
#Implementasi Dasar: Stack
#--------------------------------------------------------------

class node :
   #konstruktor yg dijalankan secara otomoatis ketika class node dipanggil
    def __init__(self, data) :
       self.data = data #menyimpan nilai/data pada list
       self.next = None #pointer ini menunjuk ke node berikutnya
       
#Stack ada operasi push(Memasukkan head baru), dan pop(Menghapus head)
class stack :
    def __init__(self) :
        self.top = None #Top menunjuk ke node paling atas (awalnya kosong)

    def isEmpty(self) : 
        return self.top is None #Stack kosong jika top = None
    
    def push(self, data) : #memasukkan data baru ke dalam stack
        #1) Membuat node baru
       nodeBaru = node(data) #memanggil konstruktor pada class node
       
       #2) Node baru menunjuk ke top yang lama
       nodeBaru.next = self.top
       
       #3) Geser top ke node baru
       self.top = nodeBaru

    def pop(self) : #menghapus node paling atas(top/head)
        if self.isEmpty() :
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        self.top = self.top.next #Geser top ke node berikutnya
        return data_terhapus

    def peek(self) : 
        #melihat data yg paling atas tanpa menghapusnya
        if self.isEmpty() :
            return None
        return self.top.data

    def tampikan(self) : 
        current = self.top
        print("Top ->", end=" ")
        while current is not None :
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Instantiasi stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampikan()
print("Peek (Lihat Top):", s.peek())
s.pop()
print("Peek (Lihat Top):", s.peek())
s.pop()
print("Peek (Lihat Top):", s.peek())