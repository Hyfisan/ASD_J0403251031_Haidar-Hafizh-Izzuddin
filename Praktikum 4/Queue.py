#==========================================================================
#Nama: Haidar Hafizh Izzuddin
#NIM: J0403251031
#Kelas: TPL A2
#==========================================================================

#--------------------------------------------------------------
#Implementasi Dasar: Queue
#--------------------------------------------------------------

class node :
   #konstruktor yg dijalankan secara otomoatis ketika class node dipanggil
    def __init__(self, data) :
       self.data = data #menyimpan nilai/data pada list
       self.next = None #pointer ini menunjuk ke node berikutnya
       
class queue :
    #Buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self) :
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang
    
    def isEmpty(self) :
        return self.front is None #Queue kosong jika front = None
    
    #Membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self, data) :
        nodeBaru = node(data)
        
        #Jika queue ksong, front dan rear menunjuk ke node yang sama 
        if self.isEmpty() :
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #Jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #Leatakkan data baru pada setelahnya rear
        self.rear = nodeBaru #Jadikan data baru sebagai rear
       
    def dequeue(self) :
        #Menghapus data dari depan(front)
        data_terhapus = self.front.data #Lihat data paling depan
        
        #Geser front ke node berikutnya
        self.front = self.front.next
        
        #Jika setelah menggeser front menjadi None, maka queue menjadi kosong, maka rear juga harus jadi none
        if self.front is None : 
            self.rear = None
        return data_terhapus
        
    def tampilkan(self) :
        current = self.front
        print("Front ->", end=" ")
        while current is not None :
            print(current.data, end=" -> ")
            current = current.next
        print("Rear") 
        
#Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
