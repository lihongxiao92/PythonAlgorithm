class CircleDeque:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.size = 0
        self.elements = [None] * self.DEFAULT_CAPACITY
        self.front = 0
    
    def index(self, index):
        index += self.front 
        if index < 0:
            return index + len(self.elements)
        return index % len(self.elements)

    def index_optimization(self, index):
        index += self.front        
        return index - (len(self.elements) if index >= len(self.elements) else 0)

    def index_rear(self):
        return self.index(self.size - 1)

    def is_empty(self):
        return self.size == 0
    
    def clear(self):
        for i in range(self.size):
            self.elements[self.index(i)] = None
        self.size = 0
        self.front = 0   
        return None

    def front(self):
        return self.elements[self.front]

    def rear(self):
        return self.elements[self.index_rear()]

    def travel(self):
        if self.size == 0:
            print("None")
            return None

        print("")

        print("length = " + str(len(self.elements)) + ", ", end= " ")
        print("size = " + str(self.size) + ", ", end= " ")
        print("front = " + str(self.front) + ", ", end= " ")     
        print("rear = " + str(self.index_rear()) + ", ", end= " ")     

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

    def enDeque_front(self, element):
        self.ensure_capacity(self.size + 1)
        self.front = self.index(-1)
        self.elements[self.front] = element
        self.size += 1
        return self.elements[self.front]

    def deDeque_front(self):
        temp_element = self.elements[self.front]
        self.elements[self.front] = None
        self.size -= 1
        self.front = self.index(1)
        return temp_element

    def enDeque_Rear(self, element):
        self.ensure_capacity(self.size + 1)
        self.elements[self.index(self.size)] = element
        self.size += 1
        return self.elements[self.index(self.size - 1)]

    def deDeque_Rear(self):
        temp_element = self.elements[self.index_rear()]
        self.elements[self.index_rear()] = None
        self.size -= 1       
        return temp_element
    
if __name__ == "__main__":
    CircleDeque1 = CircleDeque()
    for i in range(5):
        CircleDeque1.enDeque_front(i)
    # print(CircleDeque1.front())    
    CircleDeque1.travel()
    for i in range(10):
        CircleDeque1.enDeque_front(i)
    CircleDeque1.travel()
    for i in range(3):
        CircleDeque1.deDeque_front()
    CircleDeque1.travel()
    for i in range(10):
        CircleDeque1.enDeque_Rear(i)
    CircleDeque1.travel()
    for i in range(3):
        CircleDeque1.deDeque_Rear()
    CircleDeque1.travel() 