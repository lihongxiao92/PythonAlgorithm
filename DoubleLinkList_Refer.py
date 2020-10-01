"""节点"""
class Node(object):
     def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None
 """双向链表"""
class DoubleLinkList(object):
    
    def __init__(self, node=None):
        self.__head = node
"""链表是否为空""" 
    def is_empty(self):
        return self.__head is None
 
   """链表长度"""
    def length(self):
        # cur游标，用来移动遍历节点
        cur = self.__head
        # counter:记录数量
        counter = 0
        while cur != None:
            counter += 1
            cur = cur.next
        return counter
 """链表尾部添加节点，尾插法"""
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
 """链表头部添加节点，头插法"""
    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node
  """任意位置添加节点"""
    def insert(self, pos, item):
        # pos的初始值为0
        if pos <= 0:
            self.add()
        elif pos > (self.length()-1):
            self.append()
        else:
            cur = self.__head
            counter = 0
            while counter != pos:
                counter += 1
                cur = cur.next
            node = Node(item)
            node.prev = cur.prev
            cur.prev.next = node
            node.next = cur
            cur.prev = node
 """遍历整个链表"""
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")
 """根据元素删除节点"""
    def remove(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next != None:
                    # 链表不只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next != None:
                        cur.next.prev = cur.prev
                return True
            else:
                cur = cur.next
        return False
   """根据元素查找节点是否存在"""
    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
 
 
if __name__ == '__main__':
    dll = DoubleLinkList()
 
    print(dll.remove(4))
    dll.travel()
    print("----------")
    dll.append(2)
    print(dll.search(2))
    print(dll.remove(2))
    print("----------")
    dll.append(2)
    dll.append(3)
    dll.append(5)
    dll.append(6)
    dll.append(7)
    dll.travel()
    dll.add(1)
    dll.travel()
    dll.insert(3, 4)
    dll.travel()
    dll.remove(1)
    dll.travel()
    dll.remove(7)
    dll.travel()
    dll.remove(4)
    dll.travel()
    print(dll.remove(100))
    dll.travel()