# ==========================================================
# LATIHAN PRAKTIKUM LINKED LIST
# Latihan 5: Tambahkan metode untuk membalik (reverse) sebuah single linked list
#               tanpa membuat linked list baru 
#
# Nama : Haidar Hafizh Izzuddin
# NIM : J0403251031
# Kelas : TPL A2
# ==========================================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ====== MAIN PROGRAM ======
ll = LinkedList()

data_input = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")

if data_input.strip():
    numbers = list(map(int, data_input.split(",")))
    for num in numbers:
        ll.insert_at_end(num)

    print("Linked List sebelum dibalik:")
    ll.display()

    ll.reverse()

    print("Linked List setelah dibalik:")
    ll.display()
else:
    print("Linked List kosong.")
