# Python DynamicArray
class DynamicArray(object):
    DEFAULT_CAPACITY = 10
    ELEMENT_NOT_FOUND = -1

    def __init__(self, capacity):
        """
        Constructor:
                Capacity
                Size
                Data
        """
        if capacity is None or capacity < 10:
            self.capacity = self.DEFAULT_CAPACITY
        else:
            self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity

    def __getitem__(self, item):
        """
        :param item: index
        :return: self.data[item]
        """
        return self.data[item]

    def get_size(self):
        """

        :return:
        """
        return self.size

    def get_capacity(self):
        """

        :return:
        """
        return self.capacity

    def is_empty(self):
        """

        :return:
        """
        return self.size == 0

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

    def ensure_capacity(self, capacity):
        old_capacity = len(self.data)
        if old_capacity >= capacity:
            return None
        # 1.5
        new_capacity = old_capacity + (old_capacity >> 1)
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
        print(str(old_capacity) + "===> new capacity: " + str(new_capacity))

    def add(self, index, element):
        """

        :param index:
        :param element:
        :return:
        """
        self.range_check_add(index)
        # dynamic setting the capacity
        self.ensure_capacity(self.size + 1)
        # add element
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = element
        self.size += 1

    def add_last(self, element):
        self.add(self.size, element)

    def add_first(self, element):
        self.add(0, element)

    def get(self, index):
        # check if out of size
        self.range_check(index)
        return self.data[index]

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(self.size - 1)

    def set(self, index, element):
        self.range_check(index)
        self.data[index] = element

    def index_of(self, element):
        for i in range(self.size):
            if element == self.data[i]:
                return i
        else:
            return self.ELEMENT_NOT_FOUND

    def contains(self, element):
        return self.index_of(element) != self.ELEMENT_NOT_FOUND

    def find_all(self, element):
        return_list = DynamicArray(0)
        for i in range(self.size):
            if self.data[i] == element:
                return_list.add_last(i)
        return return_list.data

    def remove(self, index):
        self.range_check(index)
        remove_ele = self.data[index]
        for i in range(index + 1, self.size):
            self.data[i - 1] = self.data[i]
        self.size -= 1
        self.data[self.size] = None
        return remove_ele

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self.size-1)

    def remove_element(self, element):
        if self.index_of(element) != self.ELEMENT_NOT_FOUND:
            self.remove(self.index_of(element))

    def remove_all_element(self, element):
        while True:
            if self.index_of(element) != self.ELEMENT_NOT_FOUND:
                self.remove_element(element)
            else:
                break

    def get_max_index(self):
        max_index = 0
        for i in range(1, self.size):
            if self.data[i] > self.data[max_index]:
                max_index = i
        return max_index

    def remove_max(self):
        return self.remove(self.get_max_index())

    def get_min_index(self):
        min_index = 0
        for i in range(1, self.size):
            if self.data[i] < self.data[min_index]:
                min_index = i
        return min_index

    def remove_min(self):
        return self.remove(self.get_min_index())

    def swap(self, index1, index2):
        self.range_check(index1)
        self.range_check(index2)
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

    def print_array(self):
        for i in range(self.size):
            print(self.data[i], end=" ")
        print("\n size: %d-----capacity: %d" % (self.size, self.capacity))


if __name__ == "__main__":
    DynamicArray1 = DynamicArray(5)
    DynamicArray1.add_last(0)
    DynamicArray1.add_last(1)
    DynamicArray1.add_last(2)
    DynamicArray1.add_last(3)
    DynamicArray1.add_last(4)
    DynamicArray1.add_last(5)
    DynamicArray1.add_last(6)
    DynamicArray1.add_last(7)
    DynamicArray1.add_last(8)
    DynamicArray1.add_last(9)
    DynamicArray1.add_last(10)
    DynamicArray1.add_first(11)
    DynamicArray1.add_first(12)
    DynamicArray1.add_first(13)
    DynamicArray1.add_first(14)
    DynamicArray1.add_first(15)
    DynamicArray1.add_first(15)
    print(DynamicArray1.data)
    print(DynamicArray1.data[3])
    print(DynamicArray1.size)
    DynamicArray1.add(11, 1)
    print(DynamicArray1.data)
    print(DynamicArray1.index_of(-1))
    print(DynamicArray1.contains(16))
    print(DynamicArray1.find_all(15))
    print(DynamicArray1.swap(1, 5))
    DynamicArray1.remove_max()
    DynamicArray1.remove_max()
    for i in (range(5)):
        DynamicArray1.remove_max()
    DynamicArray1.print_array()
