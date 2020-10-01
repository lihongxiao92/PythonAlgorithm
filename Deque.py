from DoubleLinkList import DoubleLinkList


class DeQueue:
    def __init__(self):
        self.list = DoubleLinkList()

    def is_empty(self):
        return self.list.is_empty()

    def size(self):
        return self.list.size

    def enqueue_rear(self, element):
        self.list.add(self.size(), element)

    def dequeue_front(self):
        return self.list.remove(0)

    def enqueue_front(self, element):
        self.list.add(self.size(), element)

    def dequeue_rear(self):
        return self.list.remove(0)

    def front(self):
        return self.list.get(0)

    def rear(self):
        return self.list.get(0)

    def travel(self):
        self.list.travel()


if __name__ == "__main__":
    deQueue1 = DeQueue()
    deQueue1.enqueue(0)
    deQueue1.enqueue(1)
    deQueue1.enqueue(2)
    deQueue1.enqueue(3)
    deQueue1.enqueue(4)
    deQueue1.enqueue(5)
    deQueue1.travel()
    deQueue1.dequeue()
    deQueue1.dequeue()
    deQueue1.travel()

