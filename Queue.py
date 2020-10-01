from DoubleLinkList import DoubleLinkList


class Queue:
    def __init__(self):
        self.list = DoubleLinkList()

    def is_empty(self):
        return self.list.is_empty()

    def size(self):
        return self.list.size

    def enqueue(self, element):
        self.list.add(self.size(), element)

    def dequeue(self):
        return self.list.remove(0)

    def front(self):
        return self.list.get(0)

    def travel(self):
        self.list.travel()


if __name__ == "__main__":
    Queue1 = Queue()
    Queue1.enqueue(0)
    Queue1.enqueue(1)
    Queue1.enqueue(2)
    Queue1.enqueue(3)
    Queue1.enqueue(4)
    Queue1.enqueue(5)
    Queue1.travel()
    Queue1.dequeue()
    Queue1.dequeue()
    Queue1.travel()

