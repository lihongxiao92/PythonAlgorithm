class SingleLinkList:

    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.first = None
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

    def is_empty(self):
        return self.first is None

    def empty(self):
        self.first = None
        self.size = 0

    def node(self, index):
        self.range_check(index)
        node = self.first
        for i in range(index):
            node = node.next
        return node

    def add(self, index, element):
        self.range_check_add(index)
        if index == 0:
            self.first = self.Node(element, self.first)
        else:
            prev_node = self.node(index - 1)
            prev_node.next = self.Node(element, prev_node.next)
        self.size += 1

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

    def remove(self, index):
        self.range_check(index)
        node = self.first
        if index == 0:
            self.first = self.first.next
        else:
            prev_node = self.node(index - 1)
            node = prev_node.next
            prev_node.next = node.next
        self.size -= 1
        return node.element

    def set_index(self, index, element):
        self.range_check(index)
        node = self.node(index)
        node.element = element
        return node.element

    def get_index(self, index):
        self.range_check(index)
        node = self.node(index)
        return node.element

    def get_length(self):
        return self.size

    def reverse1(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverse1(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverse2(self):
        new_head = None
        current_node = self.first
        while current_node is not None:
            temp_node = current_node.next
            current_node.next = new_head
            new_head = current_node
            current_node = temp_node
        self.first = new_head

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
    SingleLinkList1 = SingleLinkList()

    SingleLinkList1.add(0, 0)
    SingleLinkList1.add(1, 1)
    SingleLinkList1.add(2, 2)
    SingleLinkList1.add(3, 3)
    SingleLinkList1.add(1, 0)
    SingleLinkList1.add(1, None)

    SingleLinkList1.travel()
    print(SingleLinkList1.index_of(None))

    print(SingleLinkList1.remove(1))
    SingleLinkList1.set_index(0, 9)
    SingleLinkList1.travel()
    SingleLinkList1.reverse2()
    SingleLinkList1.travel()
    print(SingleLinkList1.reverse1(SingleLinkList1.first))
    print(SingleLinkList1.reverse1(SingleLinkList1.first))
    print(SingleLinkList1.reverse1(SingleLinkList1.first))

    # SingleLinkList1.travel()
