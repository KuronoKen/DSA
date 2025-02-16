class DataNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        pass
class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        pass
    def insert_last(self,data):
        pointer = self.head
        if pointer:
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = DataNode(data)
        else:
            self.head = DataNode(data)
        self.count += 1
    def insert_before(self, node, data):
        pointer = self.head
        if pointer:
            before = None
            while pointer.data != node and pointer.next != None:
                before = pointer
                pointer = pointer.next
            if pointer.data == node:
                newnode = DataNode(data)
                newnode.next = pointer
                if before:
                    before.next = newnode
                else:
                    self.head = newnode
                self.count += 1
            else:
                text = "Cannot insert, " + node + " does not exist."
                print(text)
        else:
            text = "Cannot insert, " + node + " does not exist."
            print(text)
        
    def delete(self,node):
        pointer = self.head
        if pointer:
            before = None
            while pointer.data != node and pointer.next != None:
                before = pointer
                pointer = pointer.next
            if pointer.data == node:
                if pointer == self.head:
                    self.head = pointer.next
                else:
                    before.next = pointer.next
                self.count -= 1
            else:
                text = "Cannot delete, " + node + " does not exist."
                print(text)
        else:
            text = "Cannot delete, " + node + " does not exist."
            print(text)
            
    def insert_front(self,data):
        newnode = DataNode(data)
        newnode.next = self.head
        self.head = newnode
        self.count += 1
    def traverse(self):
        pointer = self.head
        output = ""
        if pointer:
            output = pointer.data
            while pointer.next != None:
                pointer = pointer.next
                output += " -> " + pointer.data
            print(output)
        else:
            print("This is an empty list.")

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    elif condition == "D":
      mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()