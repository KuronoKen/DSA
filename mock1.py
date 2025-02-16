class Song:
    def __init__(self,name,genre,dura):
        self.name = name
        self.genre = genre
        self.duration = int(dura)
        self.next = None
        pass
    def show_info(self):
        min = self.duration//60
        seconds = self.duration - (min*60)
        return self.name + " <|> " + self.genre + " <|> " + str(min) + "." + format(seconds,"02d")
    
class Queue:
    def __init__(self):
        self.head = None
        pass
    def enqueue(self, item: Song):
        if not self.head:
            self.head = item
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = item
        pass
    def dequeue(self):
        returning = None
        if self.head:
            returning = self.head
            self.head = self.head.next
            print("Dequeue item: "+returning.show_info())
        else:
            print("Underflow! Dequeue from an empty queue")
        return returning
    def peek(self):
        if self.head:
            return self.head
        else:
            print("Underflow! peek from an empty queue")
        pass
    def isEmpty(self):
        return not self.head
    def show_Queue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        pointer = self.head
        count = 1
        while pointer:
            print("Queue#" + str(count) + " " + pointer.show_info())
            pointer = pointer.next
            count += 1
        pass
    def lastSong(self,time):
        totalsec = 0
        pointer = self.head
        if pointer:
            while pointer:
                totalsec += pointer.duration
            pointer = self.head
            time = time%totalsec
            while pointer:
                time -= pointer.duration
                if time <= 0:
                    break
                pointer = pointer.next
            print(pointer.show_info())
        else:
            print("Nothing here! Please add some song")
        pass
    def removeSong(self,name):
        pointer = self.head
        former : Song = None
        while pointer:
            if pointer.name == name:
                if former:
                    former.next = pointer.next
                else:
                    self.head = None
                return
            former = pointer
            pointer = pointer.next
        print("Can not Delete! "+name+" is not exist")
                
        pass
    def groupSong(self):
        jpop = ""
        kpop = ""
        rnb = ""
        pointer = self.head
        while pointer:
            if pointer.genre == "JPOP":
                jpop += pointer.name + " | "
            elif pointer.genre == "KPOP":
                kpop += pointer.name + " | "
            elif pointer.genre == "R&B":
                rnb += pointer.name + " | "
            pointer = pointer.next
        print("JPOP: "+jpop)
        print("KPOP: "+kpop)
        print("R&B: "+rnb)
        pass
    def undo(self):
        pass
    def rev_queue(self):
        pass

def main():
    """this is main function"""
    q = Queue()
    while (choice := input()) != "End":
        command, data = choice.split(": ")
        match command:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    temp.show_info()
            case "peek":
                temp= q.peek()
                if temp:
                    temp.show_info()
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            case "rev":
                q.rev_queue()
    q.show_Queue()
main()