class DoubleCircleLinkList:

    class Node:
        def __init__(self, prev, element, next):
            self.prev = prev
            self.element = element
            self.next = next

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def range_check_add(self, index):
        """

        :param index:
        :return:
        """
        if index < 0 or index > self.size:
            self.out_of_bounds(index)

    def range_check(self, index):
        """

        :param index:
        :return:
        """
        if index < 0 or index >= self.size:
            self.out_of_bounds(index)

    def out_of_bounds(self, index):
        raise Exception("Add Filed. Require 0 <=" + "index" + "<=" + str(self.size))

    def node(self, index):
        self.range_check(index)
        if index < (self.size >> 1):
            node = self.first
            for i in range(index):
                node = node.next
        else:
            node = self.last
            for i in range(self.size - 1, index, -1):
                node = node.prev
        return node

    def index_of(self, element):
        if element is None:
            node = self.first
            for i in range(self.size):
                if node.element is None:
                    return i
                node = node.next
        else:
            node = self.first
            for i in range(self.size):
                if node.element == element:
                    return i
                node = node.next
        return -1

    @property
    def is_empty(self):
        return self.first is None

    def clear(self):
        self.size = 0
        self.first = None
        self.last = None
        return None

    def get(self, index):
        return self.node(index).element

    def set(self, index, element):
        node = self.node(index)
        node.element = element
        return node.element

    def add(self, index, element):
        self.range_check_add(index)
        if index == self.size:
            old_last = self.last
            self.last = self.Node(old_last, element, self.first)
            if old_last is None:
                self.first = self.last
                self.first.next = self.first
                self.first.prev = self.first
            else:
                old_last.next = self.last
                self.first.prev = self.last
        else:
            next_node = self.node(index)
            prev_node = next_node.prev
            node = self.Node(prev_node, element, next_node)
            next_node.prev = node
            prev_node.next = node

            if next_node == self.first:
                self.first = node

        self.size += 1

    def remove(self, index):
        self.range_check(index)
        node = self.node(index)
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            if node == self.first:
                self.first = next_node
            if node == self.last:
                self.last = prev_node

        self.size -= 1
        return node.element

    def travel(self):
        if self.size == 0:
            print("None")
            return None
        node = self.first
        for i in range(self.size):
            print(node.element, end=" ")
            node = node.next
        print("")
        print("------------------------")


if __name__ == "__main__":
    DoubleCircleLinkList1 = DoubleCircleLinkList()
    DoubleCircleLinkList1.add(0, 0)
    DoubleCircleLinkList1.add(1, 1)
    DoubleCircleLinkList1.add(2, 2)
    DoubleCircleLinkList1.add(3, 3)
    DoubleCircleLinkList1.add(1, 0)
    DoubleCircleLinkList1.add(1, None)
    DoubleCircleLinkList1.travel()
    DoubleCircleLinkList1.remove(1)
    DoubleCircleLinkList1.travel()
