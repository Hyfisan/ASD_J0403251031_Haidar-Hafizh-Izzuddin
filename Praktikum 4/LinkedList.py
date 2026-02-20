#==========================================================================
#Nama: Haidar Hafizh Izzuddin
#NIM: J0403251031
#Kelas: TPL A2
#==========================================================================


#--------------------------------------------------------------
#Implementasi Dasar: Node Pada Linked List
#--------------------------------------------------------------

class node :
   #konstruktor yg dijalankan secara otomoatis ketika class node dipanggil
    def __init__(self, data) :
       self.data = data #menyimpan nilai/data pada list
       self.next = None #pointer ini menunjuk ke node berikutnya
       
#1) Membuat node dengan instantiasi class node
nodeA = node("A")
nodeB = node("B")
nodeC = node("C")

#2) Mendefinisikan head dan Menghubungkan node: A->B->C->None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal: Menelusuri node dari head sampai ke none
current = head
while current is not None :
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya
    
    


