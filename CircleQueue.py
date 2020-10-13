class CircleQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.size = 0
        self.elements = [None] * self.DEFAULT_CAPACITY
        self.front = 0
    
    def index(self, index):
        return (self.front + index) % len(self.elements)

    def index_optimization(self, index):
        index += self.front        
        return index - (len(self.elements) if index >= len(self.elements) else 0)

    def is_empty(self):
        return self.size == 0
    
    def clear(self):
        for i in range(self.size):
            self.elements[self.index(i)] = None
        self.size = 0
        self.front = 0   

    def front(self):
        return self.elements[self.front]

    def travel(self):
        if self.size == 0:
            print("None")
            return None
        print("")
        print("length = " + str(len(self.elements)) + ", ", end= " ")
        print("size = " + str(self.size) + ", ", end= " ")
        print("front = " + str(self.front) + ", ", end= " ")        
        print(self.elements)        
        print("")
        print("------------------------")
    
    def ensure_capacity(self, capacity):
        old_capacity = len(self.elements)
        if old_capacity >= capacity:
            return None
        # 1.5
        new_capacity = old_capacity + (old_capacity >> 1)
        new_elements = [None] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[self.index(i)]
        self.elements = new_elements        
        self.front = 0

    def enqueue(self, element):
        self.ensure_capacity(self.size + 1)
        self.elements[self.index(self.size)] = element
        self.size += 1
        return self.elements[self.index(self.size)]

    def dequeue(self):
        temp_element = self.elements[self.front]
        self.elements[self.front] = None
        self.size -= 1
        self.front = self.index(1)
        return temp_element

if __name__ == "__main__":
    CircleQueue1 = CircleQueue()
    for i in range(5):
        CircleQueue1.enqueue(i)
    # print(CircleQueue1.front())    
    CircleQueue1.travel()
    for i in range(10):
        CircleQueue1.enqueue(i)
    CircleQueue1.travel()
    for i in range(3):
        CircleQueue1.dequeue()
    CircleQueue1.travel()

 
