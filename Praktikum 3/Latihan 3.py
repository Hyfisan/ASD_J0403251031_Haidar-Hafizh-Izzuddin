# ==========================================================
# LATIHAN PRAKTIKUM LINKED LIST
# Latihan 3: Implementasikan pencarian pada node tertentu double linked list
#
# Nama : Haidar Hafizh Izzuddin
# NIM : J0403251031
# Kelas : TPL A2
# ==========================================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ====== MAIN PROGRAM ======
dll = DoubleLinkedList()

data_input = input("Masukkan elemen ke dalam Double Linked List (pisahkan dengan koma): ")

if data_input.strip():
    numbers = list(map(int, data_input.split(",")))
    for num in numbers:
        dll.insert_at_end(num)

    print("Double Linked List:")
    dll.display()

    key = int(input("Masukkan elemen yang ingin dicari: "))
    if dll.search(key):
        print(f"Elemen {key} ditemukan dalam Double Linked List.")
    else:
        print(f"Elemen {key} tidak ditemukan dalam Double Linked List.")
else:
    print("Double Linked List kosong. Tidak ada elemen yang bisa dicari.")
