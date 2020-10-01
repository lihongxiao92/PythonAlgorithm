
 """定义一个节点"""
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
 
 """单向循环链表"""
class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        if node != None:
            node.next = node
 """链表是否为空"""
    def is_empty(self):
        return self.__head is None
 """链表的长度"""
    def length(self):
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量,因为循环不会进入最后一个节点所以初始值为1
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count
  """遍历整个链表"""
    def travel(self):
        cur = self.__head
        if cur == None:
            return
        else:
            while cur.next != self.__head:
                print(cur.elem, end=" ")
                cur = cur.next
            # 退出循环后cur指向尾节点，但是尾节点没有打印。
            print(cur.elem)
 """链表头部添加元素"""
    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            # 或者
            # self.__head = node
            # node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 循环结束后cur指向尾节点
            node.next = self.__head
            self.__head = node
            cur.next = node
 """链表尾部添加元素"""
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 循环结束cur指向最后一个节点
            cur.next = node
            node.next = self.__head
"""指定位置添加元素:param pos 从0开始(即将链表的第一个节点记为0节点)""" 
    # pos/position:位置，方位 param:参数
    def insert(self, pos, item):
        
        # pre/previous以前的，在什么之前
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node
 """删除节点"""
    def remove(self, item):
        pre = self.__head
        cur = self.__head
        # 判断是不是空链表
        if cur == None:
            return False
        # 判断是不是头结点
        elif cur.elem == item:
            # 判断是不是只有一个节点
            if cur.next == self.__head:
                self.__head = None
                return True
            else:
                while pre.next != self.__head:
                    pre = pre.next
                self.__head = cur.next
                pre.next = self.__head
                return True
        else:
            while pre.next != self.__head:
                if pre.next.elem == item:
                    pre.next = pre.next.next
                    return True
                else:
                    pre = pre.next
            return False
 """查找节点是否存在"""
    def search(self, item):
        cur = self.__head
        # 判断是否为空链表
        if self.__head == None:
            return False
        # 判断是不是头结点
        elif cur.elem == item:
            return True
        else:
            while cur.next != self.__head:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
            # 循环退出后cur指向最后一个节点，但是没有进入最后一个节点
            if cur.elem == item:
                return True
        return False
 
 
if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.remove(4))
    sll.travel()
    print("----------")
    sll.append(2)
    print(sll.search(2))
    print(sll.remove(2))
    print("----------")
    sll.append(2)
    sll.append(3)
    sll.append(5)
    sll.append(6)
    sll.append(7)
    sll.travel()
    sll.add(1)
    sll.travel()
    sll.insert(3, 4)
    sll.travel()
    sll.remove(1)
    sll.travel()
    sll.remove(7)
    sll.travel()
    sll.remove(4)
    sll.travel()
    print(sll.remove(100))
    sll.travel()
    print(sll.search(6))