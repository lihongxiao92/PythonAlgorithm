from DynamicArray import DynamicArray


class Stack:

    def __init__(self):
        self.list = DynamicArray(None)

    def clear(self) -> None:
        self.list.remove_all_element()
        return None

    def is_empty(self):
        return self.list.is_empty()

    def size(self):
        return self.list.get_size()

    def push(self, element):
        self.list.add_last(element)

    def pop(self):
        return self.list.remove(self.list.size - 1)

    def top(self):
        return self.list.get(self.size() - 1)

    def travel(self):
        self.list.print_array()


if __name__ == "__main__":
    Stack1 = Stack()
    Stack1.push(0)
    Stack1.push(1)
    Stack1.push(2)
    Stack1.push(3)
    Stack1.push(4)
    Stack1.push(5)
    Stack1.travel()
    Stack1.pop()
    Stack1.pop()
    Stack1.travel()
