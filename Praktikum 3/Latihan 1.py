# ==========================================================
# LATIHAN PRAKTIKUM LINKED LIST
# Latihan 1: Implementasikan fungsi	untuk menghapus	node dengan	nilai tertentu
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

    def delete_node(self, key):
        temp = self.head

        # Jika node pertama adalah yang ingin dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Elemen tidak ditemukan.")
            return

        prev.next = temp.next
        temp = None
        print(f"Elemen {key} berhasil dihapus.")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ====== MAIN PROGRAM ======
ll = LinkedList()

data_input = input("Masukkan elemen (pisahkan dengan koma): ")
if data_input.strip():
    numbers = list(map(int, data_input.split(",")))
    for num in numbers:
        ll.insert_at_end(num)

print("Linked List awal:")
ll.display()

key = int(input("Masukkan elemen yang ingin dihapus: "))
ll.delete_node(key)

print("Linked List setelah penghapusan:")
ll.display()
